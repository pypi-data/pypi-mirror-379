import subprocess
import os
import sys
from ujson import dumps as json_dumps
from ujson import load as json_load
from ujson import loads as json_loads
from yaml import dump as yaml_dump

from datetime import timedelta
from datetime import datetime

from google.cloud.dataproc_v1 import ClusterControllerClient
from google.cloud.dataproc_v1 import WorkflowTemplatePlacement
from google.cloud.dataproc_v1.types import OrderedJob
from google.cloud.dataproc_v1.types import PySparkJob
from google.cloud.dataproc_v1.services.workflow_template_service.async_client import WorkflowTemplateServiceClient
from google.cloud.dataproc_v1.types.workflow_templates import WorkflowTemplate


##
# @file
# @brief Defines workflow base class.
class ZIDS_Workflow():
    def __init__(self, workflow_name: str = ""):
        """! ZIDS_Workflow initializer.
        Loads config file and initializes parameters."""

        self.wf_name = workflow_name

        file_path = sys.modules[self.__class__.__module__].__file__
        self.curr_path = file_path[:file_path.rfind("batch_files")]

        with open(self.curr_path + 'batch_files/batch_config.json') as batch_cfg_file:
            batch_config = json_load(batch_cfg_file)

        with open(self.curr_path + 'batch_files/workflows/' + self.wf_name +
                  '_workflow/config_' + self.wf_name + '.json') as wf_cfg_file:
            wf_config = json_load(wf_cfg_file)

        self.config = {**batch_config, **wf_config}

        self.user_email = ''
        env_type = os.environ.get('SPRING_PROFILES_ACTIVE')
        if (not env_type == 'production') and (not env_type == 'staging'):
            command = 'gcloud config get-value account'
            user_email = subprocess.check_output(command, shell=True).decode(sys.stdout.encoding)
            self.user_email = user_email.split("@")[0]

        if self.user_email:
            self.config['user_email'] = self.user_email

        self.default_args = [json_dumps(self.config),
                             "start_date_placeholder", "end_date_placeholder", "params_placeholder"]

        self.region = self.config['region']
        self.zone = self.region + '-b'
        self.project_id = self.config['project_id']
        self.template_id = self.config['template_id']
        self.bucket_name = self.config['bucket_name']
        self.project_name = self.config['project_name']
        self.autoscaling_policy_id = self.project_name + '-auto-scaling-policy'
        self.wf_stages = self.config['workflow_stages']

        self.unique_iteration_id = self.config['unique_iteration_id']
        self.unique_template_id = self.config['unique_template_id']
        if self.unique_template_id:
            self.template_id = f"{self.template_id}_{self.unique_template_id}"

        if self.unique_iteration_id:
            self.folder_path = os.path.join(self.project_name, self.user_email, self.wf_name,
                                            f"unique_iteration_id_{self.unique_iteration_id}")
        else:
            self.folder_path = os.path.join(self.project_name, self.user_email, self.wf_name, 'main')

        self.bucket_path = f"gs://{self.bucket_name}/{self.folder_path}"
        self.project_path = f"projects/{self.project_id}/regions/{self.region}"

        if self.config['cluster_conf']['managed_cluster']:

            # Configure initialization script
            cluster_init_action = {"executable_file": f"{self.bucket_path}"
                                                      f"/batch_files/scripts/cluster-init-actions.sh"}
            cluster_init_list = self.config['cluster_conf']['managed_cluster']['config']['initialization_actions']

            if not isinstance(cluster_init_list, list):
                cluster_init_list = []

            cluster_init_list.append(cluster_init_action)

            # Take general parameters regarding GCE configuration from the main config file, as they can be modified
            # by Jenkins when deploying the service
            master_gce_config = batch_config['cluster_conf']['managed_cluster']['config']['gce_cluster_config']
            self.config['cluster_conf']['managed_cluster']['config']['gce_cluster_config'] = master_gce_config

        # Define workflow client
        self.serv_client = WorkflowTemplateServiceClient(
            client_options={"api_endpoint": f"{self.region}-dataproc.googleapis.com:443"}
        )

        # Define extra stage parameters
        self.extra_params = json_dumps(self.config['extra_job_params'])
        # Selection between current date or batch_config.json as date
        self.instantiate_now = False if "date_str" in self.config else True

    def configure_pip_packages(self, requirements_path: str, append: bool = False):
        """Configure pip packages based on the required steps.

        Args:
            requirements_path: Path to requirements.txt file.
            append: Append requirement packages to the currently loaded ones.

        """

        with open(requirements_path) as req_file:
            required_pkg = req_file.read().splitlines()
            required_pkg = [x for x in required_pkg if "#" not in x]
            pip_packages = ' '.join(required_pkg)

        if self.config['cluster_conf']['managed_cluster']:
            # Configure pip packages
            if not append:
                self.config['cluster_conf']['managed_cluster']['config']['gce_cluster_config']['metadata'][
                    'PIP_PACKAGES'] \
                    = pip_packages
            else:
                self.config['cluster_conf']['managed_cluster']['config']['gce_cluster_config']['metadata'][
                    'PIP_PACKAGES'] \
                    += ' ' + pip_packages

    def check_cluster(self):
        """! ZIDS_Workflow get_cluster.
        Tries to locate an existing cluster. If exists, we'll use it for template instantiation.
        If not, we will use the managed cluster to create it based on configuration
        When clusters are created manually, they include the workflow name, so this function looks for it.
        If it was created automatically, then the name is generated and this function will not find it.
        """
        clusterClient = ClusterControllerClient(
            client_options={"api_endpoint": f"{self.region}-dataproc.googleapis.com:443"}
        )

        cluster_name = f"{self.config['cluster_conf']['managed_cluster']['cluster_name']}-{self.wf_name}"

        try:
            exist_cluster = clusterClient.get_cluster(
                project_id=self.project_id,
                region=self.region,
                cluster_name=cluster_name,
            )
            if exist_cluster:
                del self.config['cluster_conf']['managed_cluster']
                self.config['cluster_conf']['cluster_selector'] = {
                    "cluster_labels": {
                        "goog-dataproc-cluster-name": cluster_name
                    }
                }
        except Exception as e:
            if "404" in str(e):
                print(f"Cluster {cluster_name} not found. Will be created when workflow is instantiated")
            else:
                # If there's something other than 404, we want to know, but the flow can carry on.
                print(f'Error getting cluster: {e}. Cluster will be created on demand')

    def build_template_structure(self) -> WorkflowTemplate:
        """! ZIDS_Workflow build_template_structure.
        build a workflow template class instance, containing all available configurations, mainly the managed cluster
        configuration at this point.

            Returns:
                WorkflowTemplate() - Created template with basic arguments
        """
        cluster_config = WorkflowTemplatePlacement(self.config['cluster_conf'])

        # if results not exist
        template = WorkflowTemplate()
        template.id = self.template_id
        template.name = self.project_path + '/workflowTemplates/' + template.id
        template.placement = cluster_config
        return template

    def create_ordered_job(self, stage_dir: str, spark_properties, python_files, archive_files,
                           additional_args=[], additional_jars=[]) -> OrderedJob:
        """! ZIDS_Workflow create_ordered_job.
        Create an ordered job from a stage directory

            Args:
                stage_dir: Stage directory, should hold the main.py file and configuration
                           example: batch_files/stages/stage_write_page_list_to_big_query
                spark_properties: A list, containing different spark properties
                python_files: A list of files which hold the project code (Can be archived)
                archive_files: A list of compressed files that the stage requires
                additional_args: A list of additional arguments, to add on top of the default ones
                additional_jars: A list of additional jar files, to add on top of the default ones
            Returns:
                An ordered job
        """

        # Assume that the last part of the path is the stage name
        stage_name = stage_dir.rsplit('/', 1)[-1]

        created_stage = OrderedJob()
        pyJob = PySparkJob()
        pyJob.main_python_file_uri = f'{self.bucket_path}/{stage_dir}/main.py'
        pyJob.archive_uris = [f'{self.bucket_path}/dist/{file_name}' if file_name.find('gs:') == -1
                              else file_name for file_name in archive_files]
        pyJob.python_file_uris = [f'{self.bucket_path}/dist/{file_name}' if file_name.find('gs:') == -1
                                  else file_name for file_name in python_files]
        pyJob.properties = spark_properties
        pyJob.args = self.default_args + additional_args
        pyJob.jar_file_uris = self.default_jars + additional_jars
        created_stage.step_id = f'{self.project_name}-{stage_name}'
        created_stage.pyspark_job = pyJob
        return created_stage

    def check_template(self):
        """! Check for an existing template. If found, delete it.
        """

        exist_template = self.get_workflow_template()

        # Deleting template if it exists
        if exist_template:
            self.delete_workflow_template(exist_template)

    def create_template(self, template):
        """! Create the complete template on the remote location.
            Args:
                template: WorkflowTemplate()
        """
        try:
            result = self.serv_client.create_workflow_template(
                parent=self.project_path,
                template=template
            )
            print(f'template {template.id} created successfully')
        except Exception as e:
            print(f'Error creating template: {e}')

    def get_workflow_template(self) -> WorkflowTemplate:
        """! Get the current template
            Returns:
                WorkflowTemplate, if such was retrieved

        """

        template_name = self.project_path + '/workflowTemplates/' + self.template_id

        try:
            existing_template = self.serv_client.get_workflow_template(
                name=template_name,
            )
            print(f'template {self.template_id} retrieved successfully')
        except Exception as e:
            print(f'Cannot get template, exception: {e}')
            return None

        return existing_template

    def instantiate_template(self, template):
        """! Instantiate the template into a working workflow, overriding DAG
        Do this only on dev mode
            Args:
                template: WorkflowTemplate()
        """

        if self.instantiate_now:
            start_date = datetime.now().replace(second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
            start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        else:
            start_date_str = self.config['date_str']
            end_date_str = self.config['date_end']

        try:
            self.serv_client.instantiate_workflow_template(
                name=template.name,
                parameters={"START_DATE": start_date_str, "END_DATE": end_date_str, "PARAMS": self.extra_params}
            )
            print(f'template {template.id} instantiated successfully')
        except Exception as e:
            print(f'Error instantiating template: {e}')

    def delete_workflow_template(self, template):
        """! Delete a given template
            Args:
                template: WorkflowTemplate()
        """

        try:
            self.serv_client.delete_workflow_template(
                name=template.name,
            )
            print(f'template {template.id} deleted successfully')
        except Exception as e:
            print(f'Error deleting template: {e}')

    def create_workflow_template(self):
        """! Create the workflow template, along with all relevant stages
        """
        raise NotImplementedError

    def create_yaml_file(self, workflow_template):
        meta_msg = workflow_template._meta.parent
        workflow_str = meta_msg.to_json(workflow_template)
        clean_workflow_str = workflow_str.strip()
        workflow_json = json_loads(clean_workflow_str)
        # Remove unnecessary fields which are enums that are messing up yaml parsing. Needs to be resolved later if
        # they are needed. Import the Enum and give correct values
        del workflow_json['placement']['managedCluster']['config']['gceClusterConfig']['privateIpv6GoogleAccess']
        del workflow_json['placement']['managedCluster']['config']['masterConfig']['preemptibility']
        del workflow_json['placement']['managedCluster']['config']['workerConfig']['preemptibility']

        file_path = sys.modules[self.__class__.__module__].__file__
        curr_path = file_path[:file_path.rfind("workflow")]
        with open(curr_path + f'/workflow_{self.wf_name}.yaml', 'w') as yml:
            yaml_dump(workflow_json, yml)
