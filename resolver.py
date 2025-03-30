@strawberry.type
class Query:
    @strawberry.field
    async def patients(self, filter: Optional[str] = None) -> List[generated_types["Patient"]]:
        query = "MATCH (p:Patient) RETURN p"
        if filter:
            query += f" WHERE {filter}"
        return driver.session().run(query).data()

schema = strawberry.Schema(Query)