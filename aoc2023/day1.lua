local file = io.open("day1.txt", "r")
file = file:read("*all")
local numbers = {}
local wordnums = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" }
local sum = 0

for line in file.gmatch(file, "%S+") do
	for i = 1, #line do
		for x in pairs(wordnums) do
			if string.find(line:sub(1, i), wordnums[x]) ~= nil then
				line = string.gsub(line, wordnums[x]:sub(1, -2), x - 1)
			end
		end
	end
	local numline = line:gsub("%D+", "")
	numline = string.sub(numline, 1, 1) .. string.sub(numline, -1)
	table.insert(numbers, numline)
end

for i, num in pairs(numbers) do
	sum = sum + num
end

print(sum)
