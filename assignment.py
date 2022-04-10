from hactap.workflow_algorithm import WorkflowAlgorithm


class CarCategorize(WorkflowAlgorithm):
    def __init__(self, parameters, ai_crowd, logger):
        self.parameters = parameters
        self.ai_crowd = ai_crowd
        self.logger = logger
        return

    def generate(self, event_type, dataset, task_assignments):
        output = []
        if event_type == "initialize":
            for dataitem in dataset:
                output.append(
                    {
                        "dataitem_id": dataitem["id"],
                        "qualified_worker_type": "human"
                    }
                )
        return output

    def assign(self, task_assignments, request_args):
        picked_assignment = list(
            filter(lambda t: t["result"] is None, task_assignments)
        )[0]
        return picked_assignment["id"], {}

    def post_process(self):
        pass
