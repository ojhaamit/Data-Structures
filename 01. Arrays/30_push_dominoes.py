class Solution:
    def pushDominoes(self, dominoes):
        max_force = len(dominoes)
        # print(max_force)
        forces = [0] * len(dominoes)

        force = 0
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                force = max_force
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force
        print(forces)

        force = 0
        for i in range(len(dominoes) - 1, -1, -1):
            d = dominoes[i]
            if d == "L":
                force = max_force
            elif d == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        print(forces)

        result = ""
        for i in range(len(forces)):
            if forces[i] < 0:
                result += 'L'
            elif forces[i] > 0:
                result += "R"
            else:
                result += '.'
        return result

# dominoes = ".L.R...LR..L.."
# print(Solution().pushDominoes(dominoes))

dominoes = "RR.L"
print(Solution().pushDominoes(dominoes))