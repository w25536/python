def solution(numbers):
	return sorted(numbers)[len(numbers)-1] * sorted(numbers)[len(numbers)-2] if sorted(numbers)[len(numbers)-1] * sorted(numbers)[len(numbers)-2] > sorted(numbers)[0] * sorted(numbers)[1] else sorted(numbers)[0] * sorted(numbers)[1]
    