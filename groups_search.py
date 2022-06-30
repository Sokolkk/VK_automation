import vk_api
# https://vk.com/dev/groups.search
def vk_auth(login, password):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    return vk_session

LOGIN = 'Логин' #Логин
PASSWORD = 'пароль' #пароль
QUERY = "python" #запрос
COUNT = 1000  # до 1000
SORT = "4"
# 0 — по умолчанию;
# 1 — по скорости роста;
# 2 — по отношению дневной посещаемости к количеству пользователей;
# 3 — по отношению количества лайков к количеству пользователей;
# 4 — по отношению количества комментариев к количеству пользователей;
# 5 — по отношению количества записей в обсуждениях к количеству пользователей.
if __name__ == '__main__':
    # Авторизируемся
    vk = vk_auth(LOGIN, PASSWORD)

    rs = vk.method('groups.search', {
        'q': QUERY,
        'type': "group",
        'sort': SORT,
        'count': COUNT,
    })


    i=0
    z=[] #сохраняем выгрузку в список
    while i < 500:
            z.append(rs['items'][i]['id'])
            i+=1
    f = open(QUERY + SORT + ".txt", "a")
    f.write(str(z))
    f.close()
