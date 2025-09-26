import strawberry
from typing import Awaitable, Callable, Any, Optional, List, Union
from graphql import GraphQLError
from strawberry.extensions.field_extension import AsyncExtensionResolver
from strawberry.schema_directive import Location
from kante.types import Info
from strawberry.extensions import FieldExtension
from strawberry.schema_directive import Location
from strawberry.types.field import StrawberryField
from authentikate.base_models import JWTToken
from authentikate.protocols import UserModel, ClientModel
from typing import cast


@strawberry.schema_directive(locations=[Location.FIELD_DEFINITION])
class Auth:
    """ A directive to enforce authentication and authorization on fields."""
    required_scopes: Optional[List[str]] = strawberry.directive_field(name="required_scopes", default=None)
    required_roles: Optional[List[str]] = strawberry.directive_field(name="required_roles", default=None)

    

class AuthExtension(FieldExtension):
    """ A directive to enforce authentication and authorization on fields."""
    
    
    def __init__(self, scopes: Optional[List[str]] | str = None, roles: Optional[List[str]] = None, any_role_of: Optional[List[str]] = None , any_scope_of: Optional[List[str]] = None ) -> None:
        """Initialize the AuthExtension with optional scopes and roles."""
        if isinstance(scopes, str):
            scopes = [scopes]
        if roles and isinstance(roles, str):
            roles = [roles]
        
        self.scopes: Optional[List[str]] = scopes
        self.roles: Optional[List[str]] = roles
        self.any_role_of: Optional[List[str]] = any_role_of
        self.any_scope_of: Optional[List[str]] = any_scope_of
        
        
        
    def apply(self, field: StrawberryField) -> None:
        """Apply the Auth directive to the field.

        Args:
            field (StrawberryField): The authentication field to which the directive will be applied.
        """
        assert not field.is_subscription, "Auth directive cannot be applied to subscriptions use AuthSubscribeExtension instead."
        field.directives.append(Auth(required_scopes=self.scopes, required_roles=self.roles))

    def resolve(
        self, next_: Callable[..., Any], source: Any, info: Info, **kwargs
    ) -> Any:
        """ Resolve the field with authentication checks."""
        if not info.context.request.user:
            raise GraphQLError("Authentication required")
        
        
        try:
            token: JWTToken = info.context.request.get_extension("token")
            
            if self.scopes and not token.has_scopes(self.scopes):
                raise GraphQLError(f"User does not have the required scopes: {self.scopes}")
            
            if self.any_scope_of and not token.has_any_role(self.any_scope_of):
                raise GraphQLError(f"User does not have any of of the required scopes: {self.any_scope_of}")
            
        
            if self.roles and not token.has_roles(self.roles):
                raise GraphQLError(f"User does not have the required roles: {', '.join(self.roles)}")
            
            if self.any_role_of and not token.has_any_role(self.any_role_of):
                raise GraphQLError(f"User does not have any of the required roles: {', '.join(self.any_role_of)}")
            
            
        except KeyError:
            raise GraphQLError("Token not found in request context")
        
        
        
        return next_(source, info, **kwargs)
    
    async def resolve_async(self, next_: Callable[..., Awaitable[Any]], source: Any, info: Info, **kwargs: Any) -> Any:
        
        
        """ Resolve the field with authentication checks."""
        if not info.context.request.user:
            raise GraphQLError("Authentication required")
        
        
        try:
            token: JWTToken = info.context.request.get_extension("token")
            
            if self.scopes and not token.has_scopes(self.scopes):
                raise GraphQLError(f"User does not have the required scopes: {self.scopes}")
        
            if self.roles and not token.has_roles(self.roles):
                raise GraphQLError(f"User does not have the required roles: {', '.join(self.roles)}")
            
            
        except KeyError:
            raise GraphQLError("Token not found in request context")
        
        
        
        
        return await next_(source, info, **kwargs)
  
  
class AuthSubscribeExtension(FieldExtension):
    
    
    def __init__(self, scopes: Optional[List[str]] | str = None, roles: Optional[List[str]] = None) -> None:
        """Initialize the AuthExtension with optional scopes and roles."""
        if isinstance(scopes, str):
            scopes = [scopes]
        if roles and isinstance(roles, str):
            roles = [roles]
        
        self.scopes: Optional[List[str]] = scopes
        self.roles: Optional[List[str]] = roles
        
        
        
    def apply(self, field: StrawberryField) -> None:
        """Apply the Auth directive to the field.

        Args:
            field (StrawberryField): The authentication field to which the directive will be applied.
        """
        assert field.is_subscription, "AuthSubscribeExtension can only be applied to subscription fields."
        field.directives.append(Auth(required_scopes=self.scopes, required_roles=self.roles))

    def resolve(
        self, next_: Callable[..., Any], source: Any, info: Info, **kwargs
    ) -> Any:
        """ Resolve the field with authentication checks."""
        if not info.context.request.user:
            raise GraphQLError("Authentication required")
        
        
        try:
            token: JWTToken = info.context.request.get_extension("token")
            
            if self.scopes and not token.has_scopes(self.scopes):
                raise GraphQLError(f"User does not have the required scopes: {self.scopes}")
        
            if self.roles and not token.has_roles(self.roles):
                raise GraphQLError(f"User does not have the required roles: {', '.join(self.roles)}")
            
            
        except KeyError:
            raise GraphQLError("Token not found in request context")
        
        
        
        return next_(source, info, **kwargs)
    
    async def resolve_async(self, next_: Callable[..., Awaitable[Any]], source: Any, info: Info, **kwargs: Any) -> Any:
        
        
        """ Resolve the field with authentication checks."""
        if not info.context.request.user:
            raise GraphQLError("Authentication required")
        
        
        try:
            token: JWTToken = info.context.request.get_extension("token")
            
            if self.scopes and not token.has_scopes(self.scopes):
                raise GraphQLError(f"User does not have the required scopes: {self.scopes}")
        
            if self.roles and not token.has_roles(self.roles):
                raise GraphQLError(f"User does not have the required roles: {', '.join(self.roles)}")
            
            
        except KeyError:
            raise GraphQLError("Token not found in request context")
        
        
        
        # this is a workaround for the fact that strawberry does not support async resolvers for subscriptions
        return next_(source, info, **kwargs)  
    
    
    
    
all_directives = [Auth]