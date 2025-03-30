import yaml
import strawberry
from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password"))

def load_schema():
    with open("schema_config.yml") as f:
        return yaml.safe_load(f)

def generate_types(schema):
    types = {}
    for type_name, config in schema["types"].items():
        fields = {}
        # Add properties
        for prop in config["properties"]:
            fields[prop] = strawberry.auto()
        # Add relationships
        for rel in config.get("relationships", []):
            target_type = rel["target"]
            rel_name = rel["name"]
            field_type = strawberry.List(types[target_type])
            fields[rel_name.lower()] = strawberry.field(
                resolver=lambda self, info, target_type=target_type, rel_name=rel_name: 
                    driver.session().run(
                        f"MATCH (n)-[:{rel_name}]->(m:{target_type}) WHERE n.id = $id RETURN m",
                        id=self.id
                    ).data()
            )
        types[type_name] = strawberry.type(type(type_name, (), fields))
    return types

schema_data = load_schema()
generated_types = generate_types(schema_data)