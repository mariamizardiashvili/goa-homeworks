# ცვლადის ტიპების შესამოწმებლად type() ფუნქციის გამოყენების დემონსტრირება.
global_var = "I'm global"#Global variable

def local_var_example():
    local_var = "I'm local"#Local variable
    print(global_var)#Print global var
    print(local_var)#Print local var

local_var_example()