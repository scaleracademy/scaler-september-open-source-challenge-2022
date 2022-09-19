class CommandLine
{
	public static void main(String ar[])
	{
		int a = Integer.parseInt(ar[0]);
		int b = Integer.parseInt(ar[1]);
		switch(ar[2])
		{
			case "+":
				System.out.println("Result is:"+(a+b));
				break;
			case "-":
				System.out.println("Result is:"+(a-b));
				break;
			case "*":
				System.out.println("Result is:"+(a*b));
				break;
			case "/":
				System.out.println("Result is:"+((float)a/b));
				break;
			case "%":
				System.out.println("Result is:"+(a%b));
				break;
			default:
				System.out.println("invalid operator");
				break;		
		}
	}
}