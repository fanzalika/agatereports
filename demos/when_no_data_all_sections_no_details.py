from agatereports.sample.adapters.MysqlAdapter import MysqlAdapter
from agatereports.sample.engine.basePage import BaseClass


def when_no_data_all_sections_no_details_sample():
    """
    When no data, all sections no details sample.

    What to do when datasource is specified but the query return is specified in 'All Sections No Details' on a report.
    In this sample, sql query is set to 'SELECT * FROM address WHERE id < 1' to return no result.

    Below are possible values of 'When No Data Type' and description of what will happen.
    Value                       Description
    <NULL>                      no report is generated (no file is created). (default)
    'No Pages'                  same as <NULL>. no report is generated (no file is created).
    'Blank Page'                a blank report is generated.
    'All Sections No Detail'    a report is generated with all bands except 'detail' and 'No Data' bands.
    'No Data Section'           a report is generated with content of the 'No Data' band.

    WARNING: Before running this sample, schema 'agatereports' must be create and populated.
    Run scripts in directory 'agatereports/tests/database/mysql' to create and populated database tables.

    CAUTION: Edit values of 'host' and 'port' to those in your environment.
     """
    print('running when no data no pages sample')
    jrxml_filename = '../demos/jrxml/when_no_data_all_sections_no_details.jrxml'  # input jrxml filename
    output_filename = '../demos/output/when_no_data_all_sections_no_details.pdf'  # output pdf filename

    # MySQL datasource
    config = {'host': 'localhost', 'port': '3306', 'user': 'python', 'password': 'python', 'database': 'agatereports'}
    data_source = MysqlAdapter(**config)

    pdf_page = BaseClass(jrxml_filename=jrxml_filename, output_filename=output_filename, data_source=data_source)
    pdf_page.generate_report()


if __name__ == '__main__':
    when_no_data_all_sections_no_details_sample()
