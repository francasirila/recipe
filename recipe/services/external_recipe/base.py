from abc import ABC, abstractmethod 


class ExternalRecipeProvider(ABC): 
    @abstractmethod 
    async def search( self, query: str ): 
        pass 
        

    @abstractmethod 
    async def get_by_id( self, recipe_id: str ): 
        pass 
        

    @abstractmethod 
    async def random( self ): 
        pass 


    @abstractmethod 
    async def search_by_ingredient( self, ingredient: str ): 
        pass 


        
    @abstractmethod 
    async def categories( self ): 
        pass