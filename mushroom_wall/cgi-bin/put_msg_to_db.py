
import wall_model
import cgi

form_data = cgi.FieldStorage()
wall_model.put_text(form_data['name'].value, form_data['content'].value)