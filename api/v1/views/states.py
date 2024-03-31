#!/usr/bin/python3
"""A new view for the State objects."""

from models.state import State
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_state.yml', methods=['GET'])
def get_states():
    """
    Gets the list of all the State objs.
    """
    _states = storage.all(State).values()
    states_list = []
    for state in _states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id_state.yml', methods=['get'])
def get_state(state_id):
    """Gets a State with the specified id."""
    _state = storage.get(State, state_id)
    if not _state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/state/delete_state.yml', methods=['DELETE'])
def delete_state(state_id):
    """
    Deletes the specified state_id.
    """

    _state = storage.get(State, state_id)

    if not _state:
        abort(404)

    storage.delete(_state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
@swag_from('documentation/state/post_state.yml', methods=['POST'])
def post_state():
    """
    Creates a new State object.
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    value = request.get_json()
    obj_instance = State(**value)
    obj_instance.save()
    return make_response(jsonify(obj_instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put_state.yml', methods=['PUT'])
def put_state(state_id):
    """
    Updates the specific State with the state_id.
    """
    _state = storage.get(State, state_id)

    if not _state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignored_keys = ['id', 'created_at', 'updated_at']

    values = request.get_json()
    for key, value in values.items():
        if key not in ignored_keys:
            setattr(_state, key, value)
    storage.save()
    return make_response(jsonify(_state.to_dict()), 200)
