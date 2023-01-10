// var elf = 0;
// var elves = new List<int>();

// foreach (var line in System.IO.File.ReadLines("day01.txt")) {
//     if (!string.IsNullOrWhiteSpace(line))
//         elf += int.Parse(line);
//     else
//     {
//         elves.Add(elf);
//         elf = 0;
//     }
// }
// elves.Add(elf);

var elves = System.IO.File.ReadAllText("day01.txt").Split("\n\n").Select(x => x.Split("\n").Select(int.Parse).Sum()).ToList();

elves.Sort((a, b) => b.CompareTo(a));

Console.WriteLine(elves.First());       //  68442
Console.WriteLine(elves.Take(3).Sum()); // 204837