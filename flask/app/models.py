from app.database import get_db

class Cuento:
    def __init__(self, id_cuento=None, nombre=None, descripcion=None, fecha_creacion=None, completada=None, activa=None):
        self.id_cuento = id_cuento
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.completada = completada
        self.activa = activa

    @staticmethod
    def __get_cuentos_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        cuentos = []
        for row in rows:
            cuentos.append(
                Cuento(
                    id_cuento=row[0],
                    nombre=row[1],
                    descripcion=row[2],
                    fecha_creacion=row[3],
                    completada=row[4],
                    activa=row[5]
                )
            )
        cursor.close()
        return cuentos

    @staticmethod
    def get_all_pending():
        return Cuento.__get_cuentos_by_query(
            """
                SELECT * 
                FROM cuentos 
                WHERE activa = true AND completada = false
                ORDER BY fecha_creacion DESC
            """
        )

    @staticmethod
    def get_all_completed():
        return Cuento.__get_cuentos_by_query(
            """
                SELECT * 
                FROM cuentos 
                WHERE activa = true AND completada = true
                ORDER BY fecha_creacion DESC
            """
        )

    @staticmethod
    def get_all_archived():
        return Cuento.__get_cuentos_by_query(
            """
                SELECT * 
                FROM cuentos 
                WHERE activa = false
                ORDER BY fecha_creacion DESC
            """
        ) 
    
    @staticmethod
    def get_by_id(id_cuento):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cuentos WHERE id = %s", (id_cuento,))

        row = cursor.fetchone()
        cursor.close()

        if row:
            return Cuento(
                id_cuento=row[0],
                nombre=row[1],
                descripcion=row[2],
                fecha_creacion=row[3],
                completada=row[4],
                activa=row[5]
            )
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_cuento: # Actualizar Cuento existente
            cursor.execute(
                """
                UPDATE cuentos
                SET nombre = %s, descripcion = %s, completada = %s, activa = %s
                WHERE id = %s
                """,
                (self.nombre, self.descripcion, self.completada, self.activa, self.id_cuento))
        else: # Crear Nuevo Cuento
            cursor.execute(
                """
                INSERT INTO cuentos
                (nombre, descripcion, fecha_creacion, completada, activa)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (self.nombre, self.descripcion, self.fecha_creacion, self.completada, self.activa))
            self.id_cuento = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE tareas SET activa = false WHERE id = %s", (self.id_cuento,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id': self.id_cuento,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d'),
            'completada': self.completada,
            'activa': self.activa
        }
