from rolepermissions.roles import AbstractUserRole

class Gestor (AbstractUserRole):
    available_permissions ={
        'cadastrar_produtos':True,
        'cadastrar_Atendente':True,
        'cadastrar_fornecedor':True,
        'realizar_atendimento':True,
    }

class Atendente (AbstractUserRole):
    available_permissions ={
        'cadastrar_produtos':True,
        'cadastrar_Atendente':False,
        'cadastrar_fornecedor':False,
        'realizar_atendimento':True,

    }   
