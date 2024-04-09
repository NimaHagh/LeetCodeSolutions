defmodule Palindrome do
  def is_palindrome(number) when number < 0, do: false
  def is_palindrome(number), do: number |> integer_to_list() |> is_list_palindrome()

  defp integer_to_list(number), do: Integer.digits(number)

  defp is_list_palindrome(list) do
    list == Enum.reverse(list)
  end
end
