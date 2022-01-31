import sqlite3
import sys


def test_con():
    """Tester le connection avec la base de donnée
    Nous écrit si la connection a réussie ou non
    """

    con = sqlite3.connect("database/plateformeTraiding.db")
    if con:
        print("Connection Successful!")
    else:
        print("Connection Failed!")
        sys.exit()


def create_table_users():
    """ Créer la table des items à vendre
    Utilise un fichier.sql pour faire cela"""

    con = sqlite3.connect("database/plateformeTraiding.db")
    cursor = con.cursor()

    sql_file = open("database/requete_sql/create_table_users.sql")
    sql_as_string = sql_file.read()

    cursor.executescript(sql_as_string)


def see_bdd_users():
    """ Afficher la base de donnée
    Le résultat peut être print en interne pour visualisé la table

    :return
    String
        Le résultat de la requête
    """

    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("select * from client_table")
    result = cur.fetchall()
    # print(result)
    return result


def list_all_table():
    """
    Liste all tables in db
    :return
    String
        Le résultat de la requête
    """
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("select name from sqlite_master where type='table';")
    return cur.fetchall()


def drop_specific_table():
    """
    Supprimer une table dans la base de données
    """
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("DROP TABLE client_table")
    con.commit()
    con.close()


def insert_client_in_bdd(username, password,
                         capital, is_admin, name,
                         surname, date_creation):
    """
    Insérer un nouveau client dans la base de donnée
    :param username:
    :param capital:
    :param is_admin:
    :param name:
    :param surname:
    :param date_creation:
    String
        L'identifiant du client
    :param password:
    String
        Le mot de passe du client
    :return:
    """
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute(
        'insert into client_table'
        ' (client_username, client_password, client_capital, '
        'client_is_admin, client_name, client_surname, '
        'client_creation_date_account) '
        ' values (?, ?, ?, ?, ?, ?, ?)', [username, password, capital, is_admin,
                                          name, surname, date_creation])
    con.commit()
    con.close()


def check_identifiant_exist():
    """
    Voir les différents identiant client dans la table client
    :return
    String
        Le resultat de la requête
    """
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("select client_username from client_table")
    return cur.fetchall()


def check_identififiant_password():
    """
    Voir les éléments clients dans la table clients
    :return
    String
        Résultat de la requête
    """
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("select client_username,"
                " client_password"
                " from client_table")
    return cur.fetchall()


def create_table_actions_user():
    """ Créer la table des items à vendre
    Utilise un fichier.sql pour faire cela"""

    con = sqlite3.connect("database/plateformeTraiding.db")
    cursor = con.cursor()

    sql_file = open("database/requete_sql/create_table_actions_user.sql")
    sql_as_string = sql_file.read()

    cursor.executescript(sql_as_string)
    con.close()


def put_action_on_db(username, date, choice, quantity, transaction, multiple_buy):
    try:
        create_table_actions_user()
    except:
        pass

    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute(
        'insert into action_users_table'
        ' (action_users_client_username, action_users_date,'
        ' action_users_choice, action_users_quantity,'
        ' action_users_total_value_transaction, action_users_multiple_buy) '
        ' values (?, ?, ?, ?, ?, ?)', [username, date, choice, quantity,
                                       transaction, multiple_buy])
    con.commit()
    con.close()


def see_bdd_actions():
    """ Afficher la base de donnée
    Le résultat peut être print en interne pour visualisé la table

    :return
    String
        Le résultat de la requête
    """
    try:
        create_table_actions_user()
    except:
        pass
    con = sqlite3.connect("database/plateformeTraiding.db")
    cur = con.cursor()
    cur.execute("select * from action_users_table")
    result = cur.fetchall()
    # print(result)
    return result