import scrapy

from itemloaders.processors import Compose
from itemloaders.processors import MapCompose
from itemloaders.processors import TakeFirst

from w3lib.html import remove_tags
from .format import remove_query_url
from .format import remove_newline
from .format import remove_text
from .format import convert_html_to_list_string


class TopCVItem(scrapy.Item): 
    source = scrapy.Field(
        output_processor=TakeFirst()
    )

    job_url = scrapy.Field(
        input_processor=MapCompose(
            remove_query_url,
        ),
        output_processor=TakeFirst()
    )
    title = scrapy.Field(
        output_processor=TakeFirst()
    )

    salary_range = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Mức lương, "),
        ),
        output_processor=TakeFirst()
    )
    location = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Địa điểm, ")
        ),
        output_processor=TakeFirst()
    )

    description = scrapy.Field(
        input_processor=MapCompose(
            convert_html_to_list_string,
        ),
        output_processor=TakeFirst()
    )
    requirements = scrapy.Field(
        input_processor=MapCompose(
            convert_html_to_list_string,
        ),
        output_processor=TakeFirst()
    )
    benefit = scrapy.Field(
        input_processor=MapCompose(
            convert_html_to_list_string,
        ),
        output_processor=TakeFirst()
    )

    company_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    company_name = scrapy.Field(
        input_processor=MapCompose(
            remove_tags
        ),
        output_processor=TakeFirst()
    )
    company_avatar = scrapy.Field(
        output_processor=TakeFirst()
    )
    company_scale = scrapy.Field(
        input_processor=Compose(
            remove_newline,
            remove_text("Quy mô:, "),
        ),
        output_processor=TakeFirst()
    )
    company_address = scrapy.Field(
        input_processor=Compose(
            remove_newline,
            remove_text("Địa điểm:, ")
        ),
        output_processor=TakeFirst()
    )

    # time_left = scrapy.Field(
    #     input_processor=MapCompose(
    #         remove_newline,
    #         remove_text("Hạn nộp hồ sơ: ")
    #     ),
    #     output_processor=TakeFirst()
    # )

    position = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Cấp bậc, ")
        ),
        output_processor=TakeFirst()
    )
    experience = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Kinh nghiệm, "),
        ),
        output_processor=TakeFirst()
    )

    quantity = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Số lượng tuyển, "),
            remove_text("người"),
        ),
        output_processor=TakeFirst()
    )

    type = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Hình thức làm việc, ")
        ),
        output_processor=TakeFirst()
    )
    gender = scrapy.Field(
        input_processor=MapCompose(
            remove_tags,
            remove_newline,
            remove_text("Giới tính, ")
        ),
        output_processor=TakeFirst()
    )

    branch = scrapy.Field(
        input_processor=MapCompose(
            convert_html_to_list_string,
        ),
        output_processor=TakeFirst()
    )
