-- This lua code is a solution to day 1 of AoC 2015

local sum = 0
local file = io.open("day1.txt", "r")
file = file:read("*all")

for i = 1, string.len(file) - 1 do
	local char = file:sub(i, i)

	if char == "(" then
		sum = sum + 1
	elseif char == ")" then
		sum = sum - 1
	end

	if sum == -1 then
		print("entered basement at character " .. i)
		break
	end
end

print(sum)
