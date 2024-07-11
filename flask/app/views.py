from flask import jsonify, request
from app.models import Cuento

from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'Hola a Cuentos para Niños de Historias Tiki'
        }
    )

def get_pending_cuentos():
    cuentos = Cuento.get_all_pending()
    return jsonify([cuento.serialize() for cuento in cuentos])

def get_completed_cuentos():
    cuentos = Cuento.get_all_completed()
    return jsonify([cuento.serialize() for cuento in cuentos])

def get_archived_cuentos():
    cuentos = Cuento.get_all_archived()
    return jsonify([cuento.serialize() for cuento in cuentos])

def get_cuento(cuento_id):
    cuento = Cuento.get_by_id(cuento_id)
    if not cuento:
        return jsonify({'message': 'Cuento no encontrado'}), 404
    return jsonify(cuento.serialize())

def create_cuento():
    data = request.json
    new_cuento = Cuento(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        fecha_creacion=date.today().strftime('%Y-%m-%d'),
        completada=False,
        activa=True
    )
    new_cuento.save()
    return jsonify({'message': 'Cuento creado con éxito'}), 201

def update_cuento(cuento_id):
    cuento = Cuento.get_by_id(cuento_id)
    if not cuento:
        return jsonify({'message': 'Cuento no encontrado'}), 404
   
    data = request.json
    cuento.nombre = data['nombre']
    cuento.descripcion = data['descripcion']
    cuento.save()
    return jsonify({'message': 'Cuento actualizado con éxito'})

def archive_cuento(cuento_id):
    cuento = Cuento.get_by_id(cuento_id)
    if not cuento:
        return jsonify({'message': 'Cuento no encontrado'}), 404
   
    cuento.delete()
    return jsonify({'message': 'Cuento eliminado con éxito'})

def __complete_cuento(cuento_id, status):
    cuento = Cuento.get_by_id(cuento_id)
    if not cuento:
        return jsonify({'message': 'Cuento no encontrado'}), 404

    cuento.completada = status
    cuento.activa = True
    cuento.save()
    return jsonify({'message': 'Cuento actualizado con éxito'})

def set_complete_cuento(cuento_id):
    return __complete_cuento(cuento_id, True)

def reset_complete_cuento(cuento_id):
    return __complete_cuento(cuento_id, False)
