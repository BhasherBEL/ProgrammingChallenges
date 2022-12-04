defmodule My do
  def scoring(string) do
    case string do
      "A X" -> 1 + 3
      "A Y" -> 2 + 6
      "A Z" -> 3 + 0
      "B X" -> 1 + 0
      "B Y" -> 2 + 3
      "B Z" -> 3 + 6
      "C X" -> 1 + 6
      "C Y" -> 2 + 0
      "C Z" -> 3 + 3
    end
  end
end

File.read!('data/sample.2022.2.txt')
  |> String.split("\n")
  |> Enum.map(&My.scoring/1)
  |> Enum.sum
  |> IO.puts
