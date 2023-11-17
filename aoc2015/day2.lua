-- This lua code is a solution to day 2 of AoC 2015

local file = io.open("day2.txt", "r")
local a = { nil, nil, nil }
local counter = 1
local wrapping = 0
local ribbon = 0
file = file:read("*all")

for num in string.gmatch(file, "%x+") do
	a[counter] = tonumber(num)
	counter = counter + 1
	-- every completed line
	if counter == 4 then
		counter = 1
		table.sort(a)
		wrapping = wrapping + (2 * a[1] * a[2]) + (2 * a[1] * a[3]) + (2 * a[2] * a[3]) + (a[1] * a[2])
		ribbon = ribbon + (2 * (a[1] + a[2])) + (a[1] * a[2] * a[3])
	end
end

print(ribbon)
