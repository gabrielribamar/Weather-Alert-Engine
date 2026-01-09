def salvar_log(menssgem):
    with open('engine.log', 'a', encoding="utf-8") as f:
        f.write(menssgem + '\n')
        