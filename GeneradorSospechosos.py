class GeneradorSospechosos:

    def __init__(self, lista_ingresos):
        self.listaIngresos = lista_ingresos

    def __get_prox_entrada_mas_reciente(self, sospechosos):
        t_prox = -1
        for each in sospechosos:
            if t_prox == -1 or each.ingreso < t_prox:
                t_prox = each.ingreso
        return t_prox

    def __get_salidas_mismo_tiempo(self, sospechosos):
        t = sospechosos[0].salida
        count = 0
        for each in sospechosos:
            if each.salida == t:
                count = count + 1
            if each.salida > t:
                break
        return count

    def encontrar_sospechosos(self):
        lista_de_listas = []
        sospechosos = []
        t_inicio_robo = -1

        for person in self.listaIngresos:
            t_actual = person.ingreso
            i = 0

            # Veo si alguien salio
            while i < len(sospechosos):  # no uso for...in... porque si saco, avanza y no revisa de nuevo esa posicion
                each = sospechosos[i]
                if each.salida <= t_actual:
                    to_remove = self.__get_salidas_mismo_tiempo(sospechosos)  # tengo que sacar todos los que
                                                                              # salida < actual al mismo timepo
                    if 5 < len(sospechosos) <= 10 and t_actual - t_inicio_robo >= 40:
                        lista_de_listas.append(sospechosos.copy())
                    for i in range(to_remove):
                        sospechosos.pop(0)  # porque esta ordenado
                    t_inicio_robo = self.__get_prox_entrada_mas_reciente(sospechosos)
                else:
                    i = i + 1

            # Agrego al nuevo
            if t_inicio_robo == -1 or t_actual > t_inicio_robo + 120:
                sospechosos.clear()
                t_inicio_robo = t_actual
            elif not sospechosos:
                t_inicio_robo = t_actual
            sospechosos.append(person)
            sospechosos.sort(key=lambda x: x.salida, reverse=False)

        # veo si cuando termino el log, el conjunto final es sospechoso
        if 5 <= len(sospechosos) <= 10:
            t_primero_que_sale = sospechosos[0].salida  # porque esta ordenado por salida
            if 40 <= t_primero_que_sale - t_inicio_robo <= 120:
                lista_de_listas.append(sospechosos)

        return lista_de_listas
