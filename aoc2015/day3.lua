-- This lua code is a solution to day 3 of AoC 2015

local coords = { 0, 0 }
local allcoords = {}
local file = io.open("day3.txt", "r")
file = file:read("*all")

local function symboltonum(num)
	if num == "^" or num == ">" then
		return 1
	elseif num == "v" or num == "<" then
		return -1
	end
end

for i = 1, string.len(file) - 1 do
	local char = file:sub(i, i)

	if char == "<" or char == ">" then
		coords[1] = coords[1] + symboltonum(char)
	else
		coords[2] = coords[2] + symboltonum(char)
	end
	table.insert(allcoords, coords[1] .. coords[2])
end

table.sort(allcoords)
local startnum = allcoords[1]

for index, value in ipairs(allcoords) do
	print(index, value)
end

-- for i = 1, #allcoords do
-- print(allcoords[i])
-- end
