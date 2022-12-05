class GradesService():    
    def get_avarage(self, notas):
        sum = 0
        for i in range(len(notas)):
            sum += notas[i]
        
        avg = sum / len(notas)
        return avg
    
    def get_points_to_add(self, avarage):
        points = 0

        if 1 <= avarage <= 5:
            points += 5
        elif 6 <= avarage <= 8:
            points += 8
        elif 9 <= avarage <= 10:
            points += 10
        
        return points