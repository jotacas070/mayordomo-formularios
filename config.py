# config.py - Configuración centralizada de formularios

# Configuración API
FLOWISE_API_URL = "https://flowiseai-railway-production-eb75.up.railway.app/api/v1/prediction/0b96fddb-9b55-48d2-8d22-5e92b0710781"

# Configuración de formularios completos (basados en tus documentos originales)
FORMULARIOS_COMPLETOS = {
    "sancionamiento_material": {
        "nombre": "Formulario de Sancionamiento de Material",
        "titulo_oficial": "FORMULARIO DE SANCIONAMIENTO DE MATERIAL",
        "tipo": "Certificación",
        "departamento": "Centro de Abastecimiento",
        "descripcion": "Documento para sancionar y clasificar material del cargo 'Menaje y Equipo General' para destrucción o depósito",
        "campos": [
            {"id": "centro_abastecimiento", "label": "Centro de Abastecimiento", "tipo": "text", "requerido": True, 
             "descripcion": "Nombre del Centro de Abastecimiento"},
            {"id": "asesor_tec_nombre", "label": "Nombre del Asesor Técnico", "tipo": "text", "requerido": True,
             "descripcion": "Nombre completo del Asesor Técnico"},
            {"id": "uurr", "label": "UU.RR. (Unidad o Repartición)", "tipo": "text", "requerido": True,
             "descripcion": "Código o nombre de la unidad responsable"},
            {"id": "fecha_sancionamiento", "label": "Fecha de sancionamiento", "tipo": "date", "requerido": True,
             "descripcion": "Fecha en que fue sancionado el material"},
            {"id": "tipo_clasificacion", "label": "Tipo de clasificación", "tipo": "select", "requerido": True,
             "opciones": ["Para depósito", "Para destrucción", "Mixto (ambos)"],
             "descripcion": "Clasificación del material sancionado"},
            {"id": "lugar", "label": "Lugar", "tipo": "text", "requerido": True,
             "descripcion": "Ciudad o lugar donde se emite el documento"},
            {"id": "fecha_emision", "label": "Fecha de emisión", "tipo": "date", "requerido": True,
             "descripcion": "Fecha de emisión del documento"},
            {"id": "nombre_jefe_centro", "label": "Nombre Jefe Centro de Abastecimiento", "tipo": "text", "requerido": True},
            {"id": "reparticion", "label": "Repartición", "tipo": "text", "requerido": True,
             "descripcion": "Nombre de la repartición"}
        ],
        "items_list": {
            "id": "material_items", 
            "label": "Listado de Materiales", 
            "campos": ["NUS/NAS", "N°Serie", "Cantidad", "Descripción", "Valor Contable"],
            "descripcion": "Materiales a sancionar con sus datos completos"
        },
        "template_word": "sancionamiento_template.docx"
    },
    
    "guia_traspaso_inventariable": {
        "nombre": "Guía de Traspaso de Material Inventariable",
        "titulo_oficial": "GUÍA DE TRASPASO DE MATERIAL INVENTARIABLE",
        "tipo": "Guía de Traspaso",
        "departamento": "Abastecimiento", 
        "descripcion": "Documento para traspasar material inventariable entre unidades de la Armada",
        "campos": [
            {"id": "reparticion_recibe", "label": "Repartición que recibe el material", "tipo": "text", "requerido": True,
             "descripcion": "Nombre completo de la unidad que recibirá el material"},
            {"id": "documento_autorizacion", "label": "Documento de autorización", "tipo": "text", "requerido": True,
             "descripcion": "Número y tipo de documento que autoriza el traspaso"},
            {"id": "nombre_comandante_envia", "label": "Nombre del Comandante que envía", "tipo": "text", "requerido": True,
             "descripcion": "Nombre completo del Comandante de la unidad que envía"},
            {"id": "uurr_actual", "label": "UU.RR. Actual (Código)", "tipo": "text", "requerido": True,
             "descripcion": "Código de la unidad actual"},
            {"id": "nombre_uurr_futura", "label": "Nombre UU.RR. Futura", "tipo": "text", "requerido": True,
             "descripcion": "Nombre de la unidad de destino"},
            {"id": "codigo_uurr_futura", "label": "Código UU.RR. Futura", "tipo": "text", "requerido": True,
             "descripcion": "Código de la unidad de destino"},
            {"id": "observaciones", "label": "Observaciones", "tipo": "textarea", "requerido": False,
             "descripcion": "Observaciones adicionales al reverso"},
            {"id": "nombre_oficial_cargo_recibe", "label": "Oficial de Cargo que recibe", "tipo": "text", "requerido": True,
             "descripcion": "Nombre del oficial responsable del cargo en la unidad receptora"},
            {"id": "lugar_fecha", "label": "Lugar y fecha de certificación", "tipo": "text", "requerido": True,
             "descripcion": "Lugar y fecha de la certificación de recepción"}
        ],
        "items_list": {
            "id": "items_traspaso",
            "label": "Items a Traspasar",
            "campos": ["NAS/NUS", "Cantidad", "Descripción", "Sección"],
            "descripcion": "Materiales inventariables a traspasar"
        }
    },
    
    "informe_tecnico_baja": {
        "nombre": "Informe Técnico para Baja de Material",
        "titulo_oficial": "FORMULARIO DE INFORME TÉCNICO PARA PROPONER LA BAJA DE MATERIAL PERMANENTE",
        "tipo": "Informe Técnico",
        "departamento": "Unidad Operativa",
        "descripcion": "Anexo A - Informe técnico para proponer la baja de material permanente de la Armada",
        "campos": [
            {"id": "codigo_unidad", "label": "Código de Unidad", "tipo": "text", "requerido": True,
             "descripcion": "Código oficial de la unidad"},
            {"id": "nombre_unidad", "label": "Nombre UU.RR.", "tipo": "text", "requerido": True,
             "descripcion": "Nombre completo de la unidad o repartición"},
            {"id": "numero_informe", "label": "Número de Informe Técnico", "tipo": "text", "requerido": True,
             "descripcion": "Número correlativo del informe"},
            {"id": "tipo_transaccion", "label": "Tipo de Transacción", "tipo": "select", "requerido": True,
             "opciones": ["Baja por inutilidad", "Baja por obsolescencia", "Baja por siniestro", "Baja por pérdida"],
             "descripcion": "Tipo de transacción a realizar"},
            {"id": "descripcion_tecnica", "label": "Descripción Técnica del Material", "tipo": "textarea", "requerido": True,
             "descripcion": "Descripción técnica detallada del material"},
            {"id": "motivo_transaccion", "label": "Motivo de la Transacción", "tipo": "textarea", "requerido": True,
             "descripcion": "Motivo detallado de la baja propuesta"},
            {"id": "fecha", "label": "Fecha", "tipo": "date", "requerido": True,
             "descripcion": "Fecha de elaboración del informe"},
            {"id": "nombre_oficial_cargo", "label": "Oficial de Cargo", "tipo": "text", "requerido": True},
            {"id": "nombre_comandante", "label": "Comandante", "tipo": "text", "requerido": True}
        ]
    },
    
    "acta_constatacion_perdida": {
        "nombre": "Acta de Constatación de Pérdida",
        "titulo_oficial": "ACTA CONSTATACIÓN DE PÉRDIDA",
        "tipo": "Acta",
        "departamento": "Unidad Operativa",
        "descripcion": "Documento para certificar la pérdida de material fiscal del cargo 'Menaje y Equipo General'",
        "campos": [
            {"id": "uurr", "label": "UU.RR. (Unidad/Repartición)", "tipo": "text", "requerido": True,
             "descripcion": "Nombre de la unidad o repartición"},
            {"id": "motivo_perdida", "label": "Motivo de la Pérdida", "tipo": "textarea", "requerido": True,
             "descripcion": "Descripción detallada del motivo de la pérdida del material"},
            {"id": "valor_total_utm", "label": "Valor total vs 6 UTM", "tipo": "select", "requerido": True,
             "opciones": ["Inferior a 6 UTM", "Superior a 6 UTM"],
             "descripcion": "¿El valor total es inferior o superior a 6 UTM?"},
            {"id": "requiere_investigacion", "label": "Requiere Investigación Sumaria", "tipo": "select", "requerido": True,
             "opciones": ["Sí", "No"], "descripcion": "¿Corresponde instruir investigación sumaria?"},
            {"id": "lugar", "label": "Lugar", "tipo": "text", "requerido": True,
             "descripcion": "Lugar donde se emite el acta"},
            {"id": "fecha", "label": "Fecha", "tipo": "date", "requerido": True,
             "descripcion": "Fecha de emisión del acta"},
            {"id": "nombre_asesor_tecnico", "label": "Nombre Asesor Técnico", "tipo": "text", "requerido": True},
            {"id": "nombre_jefe_centro", "label": "Nombre Jefe Centro AB.", "tipo": "text", "requerido": True},
            {"id": "vb_comandante", "label": "V°B° Comandante", "tipo": "text", "requerido": True,
             "descripcion": "Nombre, apellido y grado del comandante que da el visto bueno"}
        ],
        "items_list": {
            "id": "items_perdida",
            "label": "Items Perdidos", 
            "campos": ["NUS/NAS", "Cantidad", "Descripción", "Valor Contable"],
            "descripcion": "Materiales perdidos con su valorización"
        }
    },
    
    "acta_destruccion": {
        "nombre": "Acta de Destrucción",
        "titulo_oficial": "ACTA DE DESTRUCCIÓN",
        "tipo": "Acta",
        "departamento": "Unidad Operativa",
        "descripcion": "Documento para certificar la destrucción total de items del inventario 'Menaje y Equipo General'",
        "campos": [
            {"id": "numero_acta", "label": "Número del Acta", "tipo": "text", "requerido": True,
             "descripcion": "Número correlativo del acta"},
            {"id": "año", "label": "Año", "tipo": "number", "requerido": True,
             "descripcion": "Año de emisión del acta"},
            {"id": "uurr", "label": "UU.RR. (Unidad/Repartición)", "tipo": "text", "requerido": True,
             "descripcion": "Nombre de la unidad o repartición"},
            {"id": "fecha", "label": "Fecha", "tipo": "date", "requerido": True,
             "descripcion": "Fecha de destrucción"},
            {"id": "comision_1", "label": "Comisión Miembro 1", "tipo": "text", "requerido": True,
             "descripcion": "Nombre del primer miembro de la comisión"},
            {"id": "comision_2", "label": "Comisión Miembro 2", "tipo": "text", "requerido": True,
             "descripcion": "Nombre del segundo miembro de la comisión"},
            {"id": "vb_comandante", "label": "V°B° Comandante UU.RR.", "tipo": "text", "requerido": True,
             "descripcion": "Nombre del comandante que da el visto bueno"}
        ],
        "items_list": {
            "id": "items_destruccion",
            "label": "Items a Destruir",
            "campos": ["NUS/NAS", "Cantidad", "Descripción", "N°Serie", "Sección"],
            "descripcion": "Materiales a destruir con información completa"
        }
    }
}

# Keywords para detección automática de formularios
KEYWORDS_DETECCION = {
    "sancionamiento_material": [
        "sancionar", "sancionamiento", "material", "destrucción", "depósito", 
        "baja", "clasificar", "excluir", "dar de baja"
    ],
    "guia_traspaso_inventariable": [
        "traspaso", "traspasar", "transferir", "enviar", "material", 
        "inventariable", "unidad", "trasladar", "mover equipos"
    ],
    "informe_tecnico_baja": [
        "informe", "técnico", "baja", "material", "permanente", "proponer", 
        "inutilidad", "obsolescencia", "siniestro"
    ],
    "acta_constatacion_perdida": [
        "pérdida", "perdido", "constatación", "faltante", "extraviado",
        "desaparecido", "no encontrado"
    ],
    "acta_destruccion": [
        "destrucción", "destruir", "eliminar", "acta destrucción",
        "dar de baja por destrucción"
    ]
}

# Configuración de la aplicación
APP_CONFIG = {
    "titulo": "Mayordomo General IA - Gestión de Formularios",
    "subtitulo": "Sistema Inteligente de Formularios Oficiales de la Armada de Chile",
    "version": "1.0.0",
    "autor": "Mayordomo General IA",
    "descripcion": "Aplicación para gestión inteligente de formularios oficiales con integración RAG"
}