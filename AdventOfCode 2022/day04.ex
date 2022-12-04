File.read!("data/input.2022.4.txt")
  |> String.split("\n")
  |> Enum.map(
    fn line ->
      String.split(line, ",")
        |> Enum.map(fn x -> String.split(x, "-") end)
        |> List.flatten()
        |> Enum.map(&String.to_integer/1)
    end
  )
  |> Enum.filter(fn [a, b, c, d] -> a >= c and b <= d or c >= a and d <= b end)
  |> length()
  |> IO.puts()

File.read!("data/input.2022.4.txt")
  |> String.split("\n")
  |> Enum.map(
    fn line ->
      String.split(line, ",")
        |> Enum.map(fn x -> String.split(x, "-") end)
        |> List.flatten()
        |> Enum.map(&String.to_integer/1)
    end
  )
  |> Enum.filter(fn [a, b, c, d] -> c <= a and a <= d or c <= b and b <= d or a <= c and c <= b or a <= d and d <= b end)
  |> length()
  |> IO.puts()
