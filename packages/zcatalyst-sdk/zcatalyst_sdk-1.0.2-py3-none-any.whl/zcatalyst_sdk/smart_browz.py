from typing import Union, List
from .types import Component
from .exceptions import BrowserLogicError
from ._http_client import AuthorizedHttpClient
from . import validator
from ._constants import (
    RequestMethod,
    CredentialUser,
    Components,
    CatalystService
)
from .types.smart_browz import (
    DataverseEnrichLeadReq,
    DataverseLead,
    DataverseSimilarCompanyReq,
    DataverseTechStack,
    OutputOptions,
    PdfOptions,
    PdfPageOptions,
    ScreenShotOptions,
    ScreenShotPageOptions,
    NavigationOptions
)


class SmartBrowz(Component):
    def __init__(self, app) -> None:
        self._app = app
        self._requester = AuthorizedHttpClient(self._app)

    def get_component_name(self):
        return Components.SMART_BROWZ

    def convert_to_pdf(
        self,
        source: str,
        pdf_options: PdfOptions  = None,
        page_options: PdfPageOptions = None,
        navigation_options: NavigationOptions = None,
        **kwargs
    ):
        '''
        convert the given source into pdf
        '''

        req_json = {"output_options": {"output_type": "pdf"}}
        validator.is_non_empty_string(source, 'source', BrowserLogicError)
        if validator.is_valid_url(source):
            req_json['url']=source
        else:
            req_json['html']=source

        req_json.update({
            "pdf_options": pdf_options,
            "page_options": page_options,
            "navigation_options": navigation_options
        })
        req_json.update(kwargs)

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/convert',
            json=req_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        return resp.response

    def take_screenshot(
        self,
        source: str,
        screenshot_options: ScreenShotOptions = None,
        page_options: ScreenShotPageOptions = None,
        navigation_options: NavigationOptions = None,
        **kwargs
    ):
        '''
        Take screenshot of the given source
        '''

        req_json = {"output_options": {"output_type": "screenshot"}}
        validator.is_non_empty_string(source, 'source', BrowserLogicError)
        if validator.is_valid_url(source):
            req_json['url']=source
        else:
            req_json['html']=source

        req_json.update({
            "screenshot_options": screenshot_options,
            "page_options": page_options,
            "navigation_options": navigation_options
        })
        req_json.update(kwargs)

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/convert',
            json=req_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        return resp.response

    def generate_from_template(
        self,
        template_id: Union[str, int],
        template_data: dict = None,
        output_options: OutputOptions = None,
        pdf_options: PdfOptions  = None,
        screenshot_options: ScreenShotOptions = None,
        page_options: Union[PdfPageOptions, ScreenShotPageOptions] = None,
        navigation_options: NavigationOptions = None,
        **kwargs
    ):
        '''
        Generate outputs using existing templates with dynamic template datas
        '''

        validator.is_non_empty_string_or_number(template_id, 'template_id', BrowserLogicError)

        req_json = {
            "template_id": template_id,
            "template_data": template_data,
            "output_options": output_options,
            "pdf_options": pdf_options,
            "screenshot_options": screenshot_options,
            "page_options": page_options,
            "navigation_options": navigation_options
        }
        req_json.update(kwargs)

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/convert',
            json=req_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        return resp.response

    def get_enriched_lead(
        self,
        lead_critiria: DataverseEnrichLeadReq
    ) -> List[DataverseLead]:
        '''
        Get comprehensive details about any organization using its name, \
              email address or website URL.
        '''

        request_json = lead_critiria

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/dataverse/lead-enrichment',
            json= request_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        data = resp.response_json.get('data')
        return data

    def find_tech_stack(
        self,
        website_url: str
    ) -> List[DataverseTechStack]:
        '''
        Get details about the technologies and frameworks used by an organization.
        '''

        request_json = {
            "website_url": website_url
        }

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/dataverse/tech-stack-finder',
            json=request_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        data = resp.response_json.get('data')
        return data

    def get_similar_companies(
        self,
        lead_critiria: DataverseSimilarCompanyReq
    ) -> List[str]:
        '''
        Find out all the potential competitors of an organization.
        '''

        req_json = lead_critiria

        resp = self._requester.request(
            method=RequestMethod.POST,
            path='/dataverse/similar-companies',
            json=req_json,
            user=CredentialUser.ADMIN,
            catalyst_service=CatalystService.BROWSER360
        )
        data = resp.response_json.get('data')
        return data
