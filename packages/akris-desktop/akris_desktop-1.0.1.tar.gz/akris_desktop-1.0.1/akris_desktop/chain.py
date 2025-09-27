from treelib import Node, Tree


class Chain:
    def __init__(self):
        self.chain = Tree()
        self.chain.create_node("root", "root")

    def add_message(self, message):
        # if the tree is empty, add the message as a child of root
        if self.chain.children("root") == []:
            self.chain.create_node(
                message["message_hash"],
                message["message_hash"],
                parent="root",
                data=message,
            )
            return

        # if the message is an antecedent (message_hash == net_chain), insert it at the top and reassign the children
        # search for descendants of the message
        def filter_function(node):
            if node.data:
                return node.data["net_chain"] == message["message_hash"]
            else:
                return False

        descendants = list(self.chain.filter_nodes(filter_function))
        if descendants:
            # insert the message at the top of the chain
            self.chain.create_node(
                message["message_hash"],
                message["message_hash"],
                parent="root",
                data=message,
            )
            # reassign the children
            for node in descendants:
                self.chain.move_node(node.identifier, message["message_hash"])

        # if the message is a descendant of a preexisting message, add it to the descendants
        else:
            self.chain.create_node(
                message["message_hash"],
                message["message_hash"],
                parent=message["net_chain"],
                data=message,
            )

    def index(self, message_hash):
        expansion = self.chain.expand_tree(
            mode=Tree.WIDTH, sorting=True, key=self.sort_by_timestamp
        )
        for index, id in enumerate(expansion):
            if id == message_hash:
                return self.indexize(index)

    def sort_by_timestamp(self, node):
        timestamp = node.data["timestamp"]
        return timestamp

    def indexize(self, index):
        return str(float(index))
