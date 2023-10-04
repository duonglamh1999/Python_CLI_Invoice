import jinja2

from datetime import date, timedelta
import pdfkit

import read
import util


def get_context(year: int, month: int):
    sender_name = util.read_config("sender_name")
    sender_address = util.read_config("sender_address")
    sender_phone = util.read_config("sender_phone")
    customer_name = util.read_config("customer_name")
    invoice_number = f"1001{month%10}"

    invoice_date = date.today().strftime("%m/%d/%y")
    due_date = (date.today() + timedelta(days=30)).strftime("%m/%d/%y")
    csv_path = util.get_path(year,month)
    file_path = csv_path + ".csv"
    df = read.read(file_path)
    invoice_amount = sum(df.loc[:,"Total"].values)
    print(invoice_amount)
    records = df.to_dict('records')
    return {
        "sender_name": sender_name,
        "sender_address": sender_address,
        "sender_phone": sender_phone,
        "customer_name": customer_name,
        "invoice_number": invoice_number,
        "invoice_amount": invoice_amount,
        "invoice_date": invoice_date,
        "due_date": due_date,
        "df": records,
        "total_amount": invoice_amount
    }


def populate(year: int, month: int):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    TEMPLATE_FILE = "invoice.html"
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(TEMPLATE_FILE)
    context = get_context(year, month)
    html = template.render(data=context)
    css = 'style.css'
    out_path = f'{util.read_config("out_path")}{context["invoice_number"]}_invoice.pdf'
    pdfkit.from_string(html, configuration=config,output_path=out_path, css = css)

