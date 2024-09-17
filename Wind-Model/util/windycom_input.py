
def input_windycom_data():
    gradient = []
    alts = [0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000] 
    starting_time = 5
    print("\nStarting time: 8am\nIncrements of 3 hours\n")
    print("\033[1;31;40m Input -1 to exit \033[0m")
    im_goated = True
    while im_goated:
        print("Current time is " + str(starting_time))
        speeds = []
        for i in range(len(alts)):
            num = int(input("Enter the wind speed at " + str(int(alts[i])) +  "ft in kt (knots): "))
            if num == -1:
                im_goated = False
                # i guess i'm lobby :(
                break
            speeds.append(num * 1.15078)
        gradient.append([alts, speeds])
        gradient.append([alts, speeds])
        gradient.append([alts, speeds])
        starting_time += 3

    # gets rid of the empty list at the end
    if (len(gradient) > 0):
        gradient.pop()
        gradient.pop()
        gradient.pop()
    return gradient

# print(input_windycom_data())

# 5/31/24
l = [[[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 9.20624, 4.60312, 6.904679999999999, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 28.769499999999997, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 9.20624, 4.60312, 6.904679999999999, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 28.769499999999997, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 9.20624, 4.60312, 6.904679999999999, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 28.769499999999997, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 8.05546, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 8.05546, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 8.05546, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 20.714039999999997, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 20.714039999999997, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 20.714039999999997, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]]]
l2 = [[[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 12.658579999999999, 6.904679999999999, 6.904679999999999, 9.20624, 20.714039999999997, 24.166379999999997, 10.357019999999999, 20.714039999999997, 26.46794, 29.920279999999998, 31.07106, 33.37262, 31.07106, 34.523399999999995, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 12.658579999999999, 6.904679999999999, 6.904679999999999, 9.20624, 20.714039999999997, 24.166379999999997, 10.357019999999999, 20.714039999999997, 26.46794, 29.920279999999998, 31.07106, 33.37262, 31.07106, 34.523399999999995, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 12.658579999999999, 6.904679999999999, 6.904679999999999, 9.20624, 20.714039999999997, 24.166379999999997, 10.357019999999999, 20.714039999999997, 26.46794, 29.920279999999998, 31.07106, 33.37262, 31.07106, 34.523399999999995, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 14.960139999999999, 12.658579999999999, 13.809359999999998, 14.960139999999999, 18.41248, 9.20624, 18.41248, 24.166379999999997, 28.769499999999997, 32.22184, 32.22184, 32.22184, 36.82496, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 14.960139999999999, 12.658579999999999, 13.809359999999998, 14.960139999999999, 18.41248, 9.20624, 18.41248, 24.166379999999997, 28.769499999999997, 32.22184, 32.22184, 32.22184, 36.82496, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 14.960139999999999, 12.658579999999999, 13.809359999999998, 14.960139999999999, 18.41248, 9.20624, 18.41248, 24.166379999999997, 28.769499999999997, 32.22184, 32.22184, 32.22184, 36.82496, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 18.41248, 14.960139999999999, 14.960139999999999, 17.261699999999998, 18.41248, 17.261699999999998, 12.658579999999999, 20.714039999999997, 21.864819999999998, 21.864819999999998, 31.07106, 32.22184, 31.07106, 34.523399999999995, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 18.41248, 14.960139999999999, 14.960139999999999, 17.261699999999998, 18.41248, 17.261699999999998, 12.658579999999999, 20.714039999999997, 21.864819999999998, 21.864819999999998, 31.07106, 32.22184, 31.07106, 34.523399999999995, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 18.41248, 14.960139999999999, 14.960139999999999, 17.261699999999998, 18.41248, 17.261699999999998, 12.658579999999999, 20.714039999999997, 21.864819999999998, 21.864819999999998, 31.07106, 32.22184, 31.07106, 34.523399999999995, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [18.41248, 23.0156, 23.0156, 17.261699999999998, 20.714039999999997, 26.46794, 25.317159999999998, 12.658579999999999, 17.261699999999998, 18.41248, 21.864819999999998, 32.22184, 33.37262, 32.22184, 31.07106, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [18.41248, 23.0156, 23.0156, 17.261699999999998, 20.714039999999997, 26.46794, 25.317159999999998, 12.658579999999999, 17.261699999999998, 18.41248, 21.864819999999998, 32.22184, 33.37262, 32.22184, 31.07106, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [18.41248, 23.0156, 23.0156, 17.261699999999998, 20.714039999999997, 26.46794, 25.317159999999998, 12.658579999999999, 17.261699999999998, 18.41248, 21.864819999999998, 32.22184, 33.37262, 32.22184, 31.07106, 27.618719999999996]]]
# final = [[[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 4.60312, 4.60312, 4.60312, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 29.920279999999998, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 4.60312, 4.60312, 4.60312, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 29.920279999999998, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [4.60312, 9.20624, 4.60312, 4.60312, 4.60312, 19.56326, 25.317159999999998, 8.05546, 17.261699999999998, 24.166379999999997, 29.920279999999998, 29.920279999999998, 32.22184, 28.769499999999997, 37.975739999999995, 21.864819999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 10.357019999999999, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 10.357019999999999, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 10.357019999999999, 9.20624, 10.357019999999999, 10.357019999999999, 12.658579999999999, 18.41248, 9.20624, 19.56326, 21.864819999999998, 32.22184, 33.37262, 34.523399999999995, 34.523399999999995, 35.67418, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 14.960139999999999, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 14.960139999999999, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 14.960139999999999, 14.960139999999999, 14.960139999999999, 18.41248, 17.261699999999998, 13.809359999999998, 21.864819999999998, 24.166379999999997, 26.46794, 35.67418, 34.523399999999995, 34.523399999999995, 36.82496, 23.0156]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [17.261699999999998, 24.166379999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 26.46794, 26.46794, 14.960139999999999, 23.0156, 25.317159999999998, 25.317159999999998, 34.523399999999995, 33.37262, 32.22184, 36.82496, 29.920279999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 21.864819999999998, 21.864819999999998, 12.658579999999999, 17.261699999999998, 31.07106, 32.22184, 11.5078, 17.261699999999998, 20.714039999999997, 20.714039999999997, 20.714039999999997, 26.46794, 35.67418, 29.920279999999998, 34.523399999999995]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 21.864819999999998, 21.864819999999998, 12.658579999999999, 17.261699999999998, 31.07106, 32.22184, 11.5078, 17.261699999999998, 20.714039999999997, 20.714039999999997, 20.714039999999997, 26.46794, 35.67418, 29.920279999999998, 34.523399999999995]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 21.864819999999998, 21.864819999999998, 12.658579999999999, 17.261699999999998, 31.07106, 32.22184, 11.5078, 17.261699999999998, 20.714039999999997, 20.714039999999997, 20.714039999999997, 26.46794, 35.67418, 29.920279999999998, 34.523399999999995]]]
# l = [[[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 2.30156, 3.4523399999999995, 5.7539, 16.11092, 17.261699999999998, 11.5078, 11.5078, 20.714039999999997, 26.46794, 29.920279999999998, 33.37262, 34.523399999999995, 35.67418, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 2.30156, 3.4523399999999995, 5.7539, 16.11092, 17.261699999999998, 11.5078, 11.5078, 20.714039999999997, 26.46794, 29.920279999999998, 33.37262, 34.523399999999995, 35.67418, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 2.30156, 3.4523399999999995, 5.7539, 16.11092, 17.261699999999998, 11.5078, 11.5078, 20.714039999999997, 26.46794, 29.920279999999998, 33.37262, 34.523399999999995, 35.67418, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 8.05546, 6.904679999999999, 9.20624, 9.20624, 17.261699999999998, 14.960139999999999, 11.5078, 21.864819999999998, 29.920279999999998, 31.07106, 31.07106, 41.428079999999994, 36.82496, 25.317159999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 8.05546, 6.904679999999999, 9.20624, 9.20624, 17.261699999999998, 14.960139999999999, 11.5078, 21.864819999999998, 29.920279999999998, 31.07106, 31.07106, 41.428079999999994, 36.82496, 25.317159999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 8.05546, 6.904679999999999, 9.20624, 9.20624, 17.261699999999998, 14.960139999999999, 11.5078, 21.864819999999998, 29.920279999999998, 31.07106, 31.07106, 41.428079999999994, 36.82496, 25.317159999999998]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 17.261699999999998, 13.809359999999998, 16.11092, 16.11092, 16.11092, 12.658579999999999, 13.809359999999998, 21.864819999999998, 32.22184, 40.2773, 43.729639999999996, 42.57886, 42.57886, 26.46794]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 17.261699999999998, 13.809359999999998, 16.11092, 16.11092, 16.11092, 12.658579999999999, 13.809359999999998, 21.864819999999998, 32.22184, 40.2773, 43.729639999999996, 42.57886, 42.57886, 26.46794]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 17.261699999999998, 17.261699999999998, 13.809359999999998, 16.11092, 16.11092, 16.11092, 12.658579999999999, 13.809359999999998, 21.864819999999998, 32.22184, 40.2773, 43.729639999999996, 42.57886, 42.57886, 26.46794]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 21.864819999999998, 21.864819999999998, 17.261699999999998, 19.56326, 23.0156, 21.864819999999998, 20.714039999999997, 19.56326, 19.56326, 31.07106, 41.428079999999994, 31.07106, 36.82496, 36.82496, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 21.864819999999998, 21.864819999999998, 17.261699999999998, 19.56326, 23.0156, 21.864819999999998, 20.714039999999997, 19.56326, 19.56326, 31.07106, 41.428079999999994, 31.07106, 36.82496, 36.82496, 27.618719999999996]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 21.864819999999998, 21.864819999999998, 17.261699999999998, 19.56326, 23.0156, 21.864819999999998, 20.714039999999997, 19.56326, 19.56326, 31.07106, 41.428079999999994, 31.07106, 36.82496, 36.82496, 27.618719999999996]]]
# list = [[[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 3.4523399999999995, 3.4523399999999995, 5.7539, 12.658579999999999, 19.56326, 12.658579999999999, 10.357019999999999, 21.864819999999998, 26.46794, 29.920279999999998, 26.46794, 26.46794, 37.975739999999995, 37.975739999999995]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 3.4523399999999995, 3.4523399999999995, 5.7539, 12.658579999999999, 19.56326, 12.658579999999999, 10.357019999999999, 21.864819999999998, 26.46794, 29.920279999999998, 26.46794, 26.46794, 37.975739999999995, 37.975739999999995]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [3.4523399999999995, 5.7539, 3.4523399999999995, 3.4523399999999995, 5.7539, 12.658579999999999, 19.56326, 12.658579999999999, 10.357019999999999, 21.864819999999998, 26.46794, 29.920279999999998, 26.46794, 26.46794, 37.975739999999995, 37.975739999999995]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 9.20624, 8.05546, 8.05546, 9.20624, 10.357019999999999, 18.41248, 12.658579999999999, 12.658579999999999, 25.317159999999998, 26.46794, 29.920279999999998, 29.920279999999998, 37.975739999999995, 36.82496, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 9.20624, 8.05546, 8.05546, 9.20624, 10.357019999999999, 18.41248, 12.658579999999999, 12.658579999999999, 25.317159999999998, 26.46794, 29.920279999999998, 29.920279999999998, 37.975739999999995, 36.82496, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 9.20624, 8.05546, 8.05546, 9.20624, 10.357019999999999, 18.41248, 12.658579999999999, 12.658579999999999, 25.317159999999998, 26.46794, 29.920279999999998, 29.920279999999998, 37.975739999999995, 36.82496, 20.714039999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [14.960139999999999, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 17.261699999999998, 17.261699999999998, 13.809359999999998, 14.960139999999999, 25.317159999999998, 27.618719999999996, 31.07106, 37.975739999999995, 37.975739999999995, 39.12652, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [14.960139999999999, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 17.261699999999998, 17.261699999999998, 13.809359999999998, 14.960139999999999, 25.317159999999998, 27.618719999999996, 31.07106, 37.975739999999995, 37.975739999999995, 39.12652, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [14.960139999999999, 17.261699999999998, 14.960139999999999, 14.960139999999999, 16.11092, 17.261699999999998, 17.261699999999998, 13.809359999999998, 14.960139999999999, 25.317159999999998, 27.618719999999996, 31.07106, 37.975739999999995, 37.975739999999995, 39.12652, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 20.714039999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 23.0156, 20.714039999999997, 19.56326, 24.166379999999997, 21.864819999999998, 23.0156, 25.317159999999998, 26.46794, 37.975739999999995, 37.975739999999995, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 20.714039999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 23.0156, 20.714039999999997, 19.56326, 24.166379999999997, 21.864819999999998, 23.0156, 25.317159999999998, 26.46794, 37.975739999999995, 37.975739999999995, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [16.11092, 20.714039999999997, 17.261699999999998, 17.261699999999998, 17.261699999999998, 23.0156, 20.714039999999997, 19.56326, 24.166379999999997, 21.864819999999998, 23.0156, 25.317159999999998, 26.46794, 37.975739999999995, 37.975739999999995, 24.166379999999997]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 21.864819999999998, 12.658579999999999, 13.809359999999998, 18.41248, 29.920279999999998, 32.22184, 19.56326, 19.56326, 19.56326, 26.46794, 26.46794, 21.864819999999998, 35.67418, 36.82496, 31.07106]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 21.864819999999998, 12.658579999999999, 13.809359999999998, 18.41248, 29.920279999999998, 32.22184, 19.56326, 19.56326, 19.56326, 26.46794, 26.46794, 21.864819999999998, 35.67418, 36.82496, 31.07106]], [[0, 330, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [13.809359999999998, 21.864819999999998, 12.658579999999999, 13.809359999999998, 18.41248, 29.920279999999998, 32.22184, 19.56326, 19.56326, 19.56326, 26.46794, 26.46794, 21.864819999999998, 35.67418, 36.82496, 31.07106]]]
# sunday = [[[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 11.5078, 9.20624, 9.20624, 9.20624, 9.20624, 14.960139999999999, 21.864819999999998, 5.7539, 5.7539, 29.920279999999998, 39.12652, 37.975739999999995, 37.975739999999995, 35.67418, 32.22184, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 11.5078, 9.20624, 9.20624, 9.20624, 9.20624, 14.960139999999999, 21.864819999999998, 5.7539, 5.7539, 29.920279999999998, 39.12652, 37.975739999999995, 37.975739999999995, 35.67418, 32.22184, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 11.5078, 9.20624, 9.20624, 9.20624, 9.20624, 14.960139999999999, 21.864819999999998, 5.7539, 5.7539, 29.920279999999998, 39.12652, 37.975739999999995, 37.975739999999995, 35.67418, 32.22184, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 8.05546, 6.904679999999999, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 12.658579999999999, 12.658579999999999, 17.261699999999998, 17.261699999999998, 39.12652, 44.880419999999994, 44.880419999999994, 47.181979999999996, 35.67418, 21.864819999999998]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 8.05546, 6.904679999999999, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 12.658579999999999, 12.658579999999999, 17.261699999999998, 17.261699999999998, 39.12652, 44.880419999999994, 44.880419999999994, 47.181979999999996, 35.67418, 21.864819999999998]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [9.20624, 8.05546, 6.904679999999999, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 12.658579999999999, 12.658579999999999, 17.261699999999998, 17.261699999999998, 39.12652, 44.880419999999994, 44.880419999999994, 47.181979999999996, 35.67418, 21.864819999999998]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 2.30156, 18.41248, 25.317159999999998, 35.67418, 35.67418, 35.67418, 41.428079999999994, 31.07106, 24.166379999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 2.30156, 18.41248, 25.317159999999998, 35.67418, 35.67418, 35.67418, 41.428079999999994, 31.07106, 24.166379999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 2.30156, 18.41248, 25.317159999999998, 35.67418, 35.67418, 35.67418, 41.428079999999994, 31.07106, 24.166379999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 4.60312, 2.30156, 14.960139999999999, 23.0156, 31.07106, 27.618719999999996, 40.2773, 39.1265, 31.07106, 31.07106]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 4.60312, 2.30156, 14.960139999999999, 23.0156, 31.07106, 27.618719999999996, 40.2773, 39.1265, 31.07106, 31.07106]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 5.7539, 4.60312, 2.30156, 14.960139999999999, 23.0156, 31.07106, 27.618719999999996, 40.2773, 39.1265, 31.07106, 31.07106]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 13.809359999999998, 13.809359999999998, 11.5078, 11.5078, 13.809359999999998, 12.658579999999999, 9.20624, 2.30156, 12.658579999999999, 21.864819999999998, 29.920279999999998, 36.82496, 36.82496, 25.317159999999998, 25.317159999999998, 35.67418]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 13.809359999999998, 13.809359999999998, 11.5078, 11.5078, 13.809359999999998, 12.658579999999999, 9.20624, 2.30156, 12.658579999999999, 21.864819999999998, 29.920279999999998, 36.82496, 36.82496, 25.317159999999998, 25.317159999999998, 35.67418]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [12.658579999999999, 13.809359999999998, 13.809359999999998, 11.5078, 11.5078, 13.809359999999998, 12.658579999999999, 9.20624, 2.30156, 12.658579999999999, 21.864819999999998, 29.920279999999998, 36.82496, 36.82496, 25.317159999999998, 25.317159999999998, 35.67418]]]
sunday3 = [[[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 11.5078, 8.05546, 6.904679999999999, 8.05546, 8.05546, 12.658579999999999, 18.41248, 8.05546, 4.60312, 28.769499999999997, 34.523399999999995, 34.523399999999995, 36.82496, 34.523399999999995, 34.523399999999995, 19.56326]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 11.5078, 8.05546, 6.904679999999999, 8.05546, 8.05546, 12.658579999999999, 18.41248, 8.05546, 4.60312, 28.769499999999997, 34.523399999999995, 34.523399999999995, 36.82496, 34.523399999999995, 34.523399999999995, 19.56326]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [8.05546, 11.5078, 8.05546, 6.904679999999999, 8.05546, 8.05546, 12.658579999999999, 18.41248, 8.05546, 4.60312, 28.769499999999997, 34.523399999999995, 34.523399999999995, 36.82496, 34.523399999999995, 34.523399999999995, 19.56326]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 5.7539, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 11.5078, 5.7539, 14.960139999999999, 26.46794, 31.07106, 32.22184, 35.67418, 35.67418, 34.523399999999995, 20.714039999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 5.7539, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 11.5078, 5.7539, 14.960139999999999, 26.46794, 31.07106, 32.22184, 35.67418, 35.67418, 34.523399999999995, 20.714039999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 8.05546, 5.7539, 6.904679999999999, 6.904679999999999, 8.05546, 10.357019999999999, 11.5078, 5.7539, 14.960139999999999, 26.46794, 31.07106, 32.22184, 35.67418, 35.67418, 34.523399999999995, 20.714039999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 6.904679999999999, 6.904679999999999, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 29.920279999999998, 23.0156, 28.769499999999997, 32.22184, 27.618719999999996, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 6.904679999999999, 6.904679999999999, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 29.920279999999998, 23.0156, 28.769499999999997, 32.22184, 27.618719999999996, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [5.7539, 6.904679999999999, 6.904679999999999, 5.7539, 5.7539, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 29.920279999999998, 23.0156, 28.769499999999997, 32.22184, 27.618719999999996, 23.0156]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 24.166379999999997, 24.166379999999997, 27.618719999999996, 24.166379999999997, 21.864819999999998, 28.769499999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 24.166379999999997, 24.166379999999997, 27.618719999999996, 24.166379999999997, 21.864819999999998, 28.769499999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 6.904679999999999, 4.60312, 3.4523399999999995, 17.261699999999998, 24.166379999999997, 24.166379999999997, 24.166379999999997, 27.618719999999996, 24.166379999999997, 21.864819999999998, 28.769499999999997]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 11.5078, 11.5078, 11.5078, 13.809359999999998, 16.11092, 9.20624, 3.4523399999999995, 11.5078, 21.864819999999998, 21.864819999999998, 20.714039999999997, 18.41248, 21.864819999999998, 14.960139999999999, 35.67418]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 11.5078, 11.5078, 11.5078, 13.809359999999998, 16.11092, 9.20624, 3.4523399999999995, 11.5078, 21.864819999999998, 21.864819999999998, 20.714039999999997, 18.41248, 21.864819999999998, 14.960139999999999, 35.67418]], [[0, 330, 1000, 2000, 2500, 3000, 5000, 6400, 10000, 14000, 18000, 24000, 30000, 34000, 39000, 45000, 98000], [11.5078, 14.960139999999999, 11.5078, 11.5078, 11.5078, 13.809359999999998, 16.11092, 9.20624, 3.4523399999999995, 11.5078, 21.864819999999998, 21.864819999999998, 20.714039999999997, 18.41248, 21.864819999999998, 14.960139999999999, 35.67418]]]
print(len(sunday3))