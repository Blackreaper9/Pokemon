from flask import Blueprint
from app.models.factory import ModelFavorite
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required 

bp = Blueprint("pokemons",__name__, url_prefix="/pokemons")
RM= ResponseManager()
POKEMON_MODEL = ModelFavorite.get_model("pokemons")

@bp.route("/get/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon = POKEMON_MODEL.find_by_id(ObjectId(pokemon_id))
    return RM.success(pokemon)

@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    data = POKEMON_MODEL.find_all()
    return RM.success(data)