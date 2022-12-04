File.read!('data/sample.2022.1.txt')
  |> String.split("\n\n")
  |> Enum.map(&String.split/1)
  |> Enum.map(fn x -> Enum.map(x, &String.to_integer/1) end)
  |> Enum.map(&Enum.sum/1)
  |> Enum.max
  |> IO.puts
