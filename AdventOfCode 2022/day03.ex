File.read!('data/sample.2022.3.txt')
 |> String.split()
 |> Enum.map(&String.to_charlist/1)
 |> Enum.map(fn x -> Enum.chunk_every(x, div(length(x),2)) end)
 |> Enum.map(fn x -> hd(x) -- (hd(x) -- hd(tl(x))) end)
 |> Enum.map(fn x -> (hd(x) >= 97) && (hd(x) - 96) || (hd(x) - 65 + 27) end)
 |> Enum.sum()
 |> IO.puts()
