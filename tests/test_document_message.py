import pytest
from pydantic.error_wrappers import ValidationError
from pydantic_factories import ModelFactory

from tests.conftest import get_random_string
from whatsapp.models.core import MessageBody
from whatsapp.models.document_message import DocumentMessageBody


class DocumentMessageBodyFactory(ModelFactory):
    __model__ = DocumentMessageBody


def test_document_message_body__is_an_instance_of_message_body():
    assert isinstance(DocumentMessageBodyFactory.build(), MessageBody) is True


@pytest.mark.parametrize("content", [None, "", {}])
def test_when_content_is_invalid__validation_error_is_raised(content):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": content})


@pytest.mark.parametrize(
    "media_url", [None, "", {}, get_random_string(2049), "www.infobip.com/document"]
)
def test_when_content_media_url_is_invalid__validation_error_is_raised(media_url):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": {"mediaUrl": media_url}})


@pytest.mark.parametrize("caption", [None, "", {}, get_random_string(3001)])
def test_when_content_caption_is_invalid__validation_error_is_raised(caption):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": {"caption": caption}})


@pytest.mark.parametrize("filename", [None, "", {}, get_random_string(241)])
def test_when_content_filename_is_invalid__validation_error_is_raised(filename):
    with pytest.raises(ValidationError):
        DocumentMessageBodyFactory.build(**{"content": {"filename": filename}})