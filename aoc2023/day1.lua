local file = io.open("day1.txt", "r")
file = file:read("*all")
local numbers = {}
-- local wordnums = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero" }
local sum = 0

for line in file.gmatch(file, "%S+") do
	-- line = string.gsub(line, "zero", "0")
	local numline = line:gsub("%D+", "")
	numline = string.sub(numline, 1, 1) .. string.sub(numline, -1)
	table.insert(numbers, numline)
end

for i, num in pairs(numbers) do
	sum = sum + num
end

print(sum)
