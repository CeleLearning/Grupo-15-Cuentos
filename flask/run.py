from flask import Flask

from app.views import *
from app.database import *

app = Flask(__name__)

# Rutas de API-Rest
app.route('/', methods=['GET'])(index)

# CRUD
app.route('/api/cuentos/pending/', methods=['GET'])(get_pending_cuentos)
app.route('/api/cuentos/completed/', methods=['GET'])(get_completed_cuentos)
app.route('/api/cuentos/archived/', methods=['GET'])(get_archived_cuentos)

app.route('/api/cuentos/fetch/<int:cuento_id>', methods=['GET'])(get_cuento)

app.route('/api/cuentos/create/', methods=['POST'])(create_cuento)
app.route('/api/cuentos/update/<int:cuento_id>', methods=['PUT'])(update_cuento)

app.route('/api/cuentos/archive/<int:cuento_id>', methods=['DELETE'])(archive_cuento)
app.route('/api/cuentos/complete/set/<int:cuento_id>', methods=['PUT'])(set_complete_cuento)
app.route('/api/cuentos/complete/reset/<int:cuento_id>', methods=['PUT'])(reset_complete_cuento)

create_table_cuentos()

# Conexión a BDD
init_app(app)

# Cors
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)