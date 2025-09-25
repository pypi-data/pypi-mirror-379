"""Make data and attributes names valid identifiers

Revision ID: b24e411edc37
Revises: 337e01e5199e
Create Date: 2025-09-24 11:56:30.463786

"""

import sqlalchemy as sa
from alembic import op

from deseasion.backend.models.processing_models import _replace_variables_code
from deseasion.backend.schemas.utils import safe_attrname, safe_varname
from deseasion.backend.services.utils import progress_bar

# revision identifiers, used by Alembic.
revision = "b24e411edc37"
down_revision = "337e01e5199e"
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    vars_updates = {}

    # Get all base data except generated geo data
    nb = conn.execute(
        sa.text(
            "SELECT count(id) FROM base_data WHERE type!='generated_geo_data'"
        )
    ).fetchone()[0]
    res = conn.execute(
        sa.text(
            "SELECT id, name FROM base_data WHERE type != 'generated_geo_data'"
        )
    )
    data_updates = {}
    all_data_names = {}
    i = 0
    print("Analyze uploaded base data")
    progress_bar(i, nb)
    for id_, name in res:
        new_name = safe_varname(name)
        all_data_names[id_] = new_name
        if new_name != name:
            data_updates[id_] = new_name
        i += 1
        progress_bar(i, nb)

    if len(data_updates) > 0:
        print(f"{len(data_updates)} uploaded data to update")
        # Prepare the VALUES part of the statement
        values_clause = ", ".join(
            f"({id_}, :name_{id_})" for id_ in data_updates.keys()
        )

        # Prepare the parameters
        params = {f"name_{id_}": name for id_, name in data_updates.items()}

        # Construct and execute a single UPDATE statement
        sql = f"""
        UPDATE base_data AS b
        SET name = v.new_name
        FROM (VALUES {values_clause}) AS v(id, new_name)
        WHERE b.id = v.id
        """
        conn.execute(sa.text(sql), params)

    # Get all data attributes
    nb = conn.execute(
        sa.text("SELECT count(id) FROM data_attribute")
    ).fetchone()[0]
    res = conn.execute(sa.text("SELECT id, name, data_id FROM data_attribute"))
    attr_updates = {}
    i = 0
    print("Analyze data attributes")
    progress_bar(i, nb)
    for id_, name, data_id in res:
        new_name = safe_attrname(name)
        if new_name != name:
            attr_updates[id_] = (data_id, name, new_name)
        if new_name != name or data_id in data_updates:
            vars_updates[data_id] = vars_updates.get(data_id, [])
            vars_updates[data_id].append((id_, name, new_name))
        i += 1
        progress_bar(i, nb)

    if len(attr_updates) > 0:
        print(f"{len(attr_updates)} data attributes to update")
        # Prepare the VALUES part of the statement
        values_clause = ", ".join(
            f"({id_}, :name_{id_})" for id_ in attr_updates.keys()
        )

        # Prepare the parameters
        params = {f"name_{id_}": v[-1] for id_, v in attr_updates.items()}

        # Construct and execute a single UPDATE statement
        sql = f"""
        UPDATE data_attribute AS b
        SET name = v.new_name
        FROM (VALUES {values_clause}) AS v(id, new_name)
        WHERE b.id = v.id
        """
        conn.execute(sa.text(sql), params)

    # Get all project data
    nb = conn.execute(
        sa.text("SELECT count(id) FROM project_data")
    ).fetchone()[0]
    res = conn.execute(sa.text("SELECT id, name, data_id FROM project_data"))
    pdata_updates = {}
    input_updates = {}
    i = 0
    print("Analyze project data")
    progress_bar(i, nb)
    for id_, name, data_id in res:
        if data_id in all_data_names:
            # If project data is not a generator, use the updated data name
            new_name = all_data_names[data_id]
        else:
            new_name = safe_varname(name)
        if new_name != name:
            pdata_updates[id_] = new_name
        if data_id in vars_updates:
            input_updates[id_] = (data_id, name, new_name)
        i += 1
        progress_bar(i, nb)

    if len(pdata_updates) > 0:
        print(f"{len(pdata_updates)} project data to update")
        # Prepare the VALUES part of the statement
        values_clause = ", ".join(
            f"({id_}, :name_{id_})" for id_ in pdata_updates.keys()
        )

        # Prepare the parameters
        params = {f"name_{id_}": name for id_, name in pdata_updates.items()}

        # Construct and execute a single UPDATE statement
        sql = f"""
        UPDATE project_data AS b
        SET name = v.new_name
        FROM (VALUES {values_clause}) AS v(id, new_name)
        WHERE b.id = v.id
        """
        conn.execute(sa.text(sql), params)

    # Set generated geo data name to project data name
    conn.execute(
        sa.text(
            """
        UPDATE base_data
        SET name = p.name
        FROM project_data AS p
        WHERE base_data.type='generated_geo_data' AND base_data.id=p.data_id
    """
        )
    )

    # Get all project data with inputs changing
    nb = conn.execute(
        sa.text("SELECT count(*) FROM data_input_association")
    ).fetchone()[0]
    res = conn.execute(
        sa.text(
            "SELECT project_data_id, input_data_id FROM data_input_association"
        )
    )
    i = 0
    print("Analyze project data inputs")
    progress_bar(i, nb)
    data_model_verifs = {}
    for id_, input_id in res:
        if input_id not in input_updates:
            i += 1
            progress_bar(i, nb)
            continue
        data_model_verifs[id_] = data_model_verifs.get(id_, {})
        data_id, old_name, new_name = input_updates[input_id]
        for _, old_attrname, new_attrname in vars_updates[data_id]:
            data_model_verifs[id_][(old_name, old_attrname)] = (
                new_name,
                new_attrname,
            )
        i += 1
        progress_bar(i, nb)

    # Get all python processing models
    nb = conn.execute(
        sa.text(
            "SELECT count(id) "
            "FROM processing_model "
            "WHERE model_type='continuous_rule'"
        )
    ).fetchone()[0]
    res = conn.execute(
        sa.text(
            "SELECT id, data_generator_id, rule "
            "FROM processing_model "
            "WHERE model_type='continuous_rule'"
        )
    )
    i = 0
    print("Analyze python processing models")
    progress_bar(i, nb)
    rule_updates = {}
    for id_, data_id, rule in res:
        if data_id not in data_model_verifs:
            i += 1
            progress_bar(i, nb)
            continue
        new_rule = _replace_variables_code(rule, data_model_verifs[data_id])
        if new_rule != rule:
            rule_updates[id_] = new_rule
        i += 1
        progress_bar(i, nb)

    if len(rule_updates) > 0:
        print(f"{len(rule_updates)} python models to update")
        # Prepare the VALUES part of the statement
        values_clause = ", ".join(
            f"({id_}, :rule_{id_})" for id_ in rule_updates.keys()
        )

        # Prepare the parameters
        params = {f"rule_{id_}": rule for id_, rule in rule_updates.items()}

        # Construct and execute a single UPDATE statement
        sql = f"""
        UPDATE processing_model AS b
        SET rule = v.new_rule
        FROM (VALUES {values_clause}) AS v(id, new_rule)
        WHERE b.id = v.id
        """
        conn.execute(sa.text(sql), params)

    # Get all categories processing models
    nb = conn.execute(
        sa.text("SELECT count(id) FROM discrete_category")
    ).fetchone()[0]
    res = conn.execute(
        sa.text(
            "SELECT m.id, m.data_generator_id, c.id, c.rules "
            "FROM discrete_category c "
            "JOIN processing_model m ON m.id=c.preference_model_id"
        )
    )
    i = 0
    print("Analyze categories processing models")
    progress_bar(i, nb)
    cat_updates = {}
    for id_, data_id, cat_id, rules in res:
        if data_id not in data_model_verifs:
            i += 1
            progress_bar(i, nb)
            continue
        new_rules = [
            _replace_variables_code(rule, data_model_verifs[data_id])
            for rule in rules
        ]
        cat_updates[cat_id] = new_rules
        i += 1
        progress_bar(i, nb)

    if len(cat_updates) > 0:
        print(f"{len(cat_updates)} discrete categories to update")
        # Prepare the VALUES part of the statement
        values_clause = ", ".join(
            f"({id_}, :rules_{id_})" for id_ in cat_updates.keys()
        )

        # Prepare the parameters
        params = {f"rules_{id_}": rules for id_, rules in cat_updates.items()}

        # Construct and execute a single UPDATE statement
        sql = f"""
        UPDATE discrete_category AS b
        SET rules = v.new_rules
        FROM (VALUES {values_clause}) AS v(id, new_rules)
        WHERE b.id = v.id
        """
        conn.execute(sa.text(sql), params)


def downgrade():
    pass
