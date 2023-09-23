import jinja2

from datetime import date, timedelta
import pdfkit
import util


def get_context(year: int, month: int):
    sender_name = util.read_config("sender_name")
    sender_address = util.read_config("sender_address")
    sender_phone = util.read_config("sender_phone")
    customer_name = util.read_config("customer_name")
    invoice_number = f"1{year}{month}"
    invoice_amount = "invoice amount for now"
    invoice_date = date.today().strftime("%m/%d/%y")
    due_date = (date.today() - timedelta(days=30)).strftime("%m/%d/%y")
    return {
        "sender_name": sender_name,
        "sender_address": sender_address,
        "sender_phone": sender_phone,
        "customer_name": customer_name,
        "invoice_number": invoice_number,
        "invoice_amount": invoice_amount,
        "invoice_date": invoice_date,
        "due_date": due_date
    }


def populate(year: int, month: int):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    TEMPLATE_FILE = "invoice.html"
    print(get_context(year, month))
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(TEMPLATE_FILE)
    html = template.render(data=get_context(year, month))
    css = 'style.css'
    out_path = f'C:\\Users\\David\\Desktop\\pdf_lol.pdf'
    pdfkit.from_string(html, configuration=config,output_path=out_path, css = css)

