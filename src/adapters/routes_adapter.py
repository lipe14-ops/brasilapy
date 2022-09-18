from brasilapy.src.interfaces import IAdapter, IApiRoute


class RoutesAdapter(IAdapter):
    """create routes from a source."""

    @staticmethod
    def handle(base_url: str, api_paths: dict[str, str], route: IApiRoute) -> list[IApiRoute]:
        """ generates the client routes.

        Params:
            base_url <string>: API standard path.
            api_paths <dictionary<string, string>>: 
                API route structures (the keys are the endpoint name and the values are the endpoint path). 
        
        Returns <list<IApiRoute>>: 
            list of "IApiRoute" class objects.
        """

        return [route(name, base_url + path) for name, path in api_paths.items()]
