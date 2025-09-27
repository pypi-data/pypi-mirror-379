# src/turbopdf/assemblers/base.py
from django.template.loader import render_to_string
from turbopdf.core import generate_pdf_from_string
import turbopdf
import os

class BaseFormAssembler:
    def __init__(self, context=None):
        self.context = context or {}
        self.components = []
        self.img_base = self._get_img_base()
        self.page_number = 1
        self.total_pages = 4  # Por defecto, puedes cambiarlo si necesitas más páginas

    def _get_img_base(self):
        turbopdf_path = os.path.dirname(turbopdf.__file__)
        img_dir = os.path.join(turbopdf_path, 'img')
        img_dir = img_dir.replace('\\', '/')
        return f'file:///{img_dir}'

    def add_page_break(self):
        """Agrega un salto de página."""
        self.components.append('<div style="page-break-before: always;"></div>')
        self.page_number += 1
        return self

    def add_component(self, template_name, extra_context=None, wrapper_html=None):
        """Agrega un componente al ensamblador."""
        full_context = {
            **self.context,
            'img_base': self.img_base,
            **(extra_context or {})
        }
        
        rendered = render_to_string(f'sistema/{template_name}', full_context)
        
        if wrapper_html:
            rendered = wrapper_html.replace('{{component}}', rendered)
        
        self.components.append(rendered)
        return self

    def add_raw_html(self, html):
        """Agrega HTML crudo."""
        self.components.append(html)
        return self

    def build(self):
        # Renderizar head global
        head_context = {**self.context, 'img_base': self.img_base}
        head = render_to_string('sistema/style.html', head_context)

        # Construir el cuerpo del PDF
        body_html = "\n".join(self.components)

        # Plantilla base del formulario
        html_final = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Formulario</title>
            <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            {head}
        </head>
        <body style="font-family: 'Roboto', sans-serif; margin: 0; padding: 0;">
            <!-- Página 1 -->
            <div style="border: 1px solid #303d50; border-radius: 5px; min-height: 1170px; font-family: 'Roboto', sans-serif; page-break-after: always;">
                <!-- Encabezado -->
                {render_to_string('sistema/titulo_logo.html', {
                    'titulo1': "FORMULARIO DE RECURSO DE REPOSICIÓN",
                    'titulo2': "CONTRA RESOLUCIONES DEL COMITÉ CERREM INDIVIDUAL Y COLECTIVO",
                    'titulo3': "UNIDAD NACIONAL DE PROTECCIÓN",
                    'img_base': self.img_base
                })}
                
                <!-- Contenido -->
                {body_html}
                
                <!-- Oficialización -->
                {render_to_string('sistema/oficializacion.html', {
                    'codigo': "GJU-FT-52-VX", 
                    'fecha': "Oficialización: 00/00/0000", 
                    'pagina': f"Pág. {self.page_number} de {self.total_pages}"
                })}
            </div>
            
            <!-- Páginas adicionales -->
            <!-- Aquí puedes agregar más páginas según sea necesario -->
        </body>
        </html>
        """
        return generate_pdf_from_string(html_final)