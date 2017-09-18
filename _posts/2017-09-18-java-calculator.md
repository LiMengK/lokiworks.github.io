---
layout: post
title: 一道java的面试题
keywords:
  - java
description: 
category: java
tags:
  - java
published: true
---
{% include JB/setup %}

# 题目:用java实现一个简单的计算器
实现一个计算器大概用两种方式。一种使用栈的方式，还有一种通过构造抽象语法树的方法。本文主要讲述栈的实现方式。

## 栈实现方式的原理
通过解析文本，分别构造数值栈与操作符栈，每次分别从操作符栈中取出一个符号，从数值栈中取出两个数值。然后将计算出的结果放入数值栈中。重复执行上述操作直到符号栈为空。

## 代码示例
**Priority.java**
```java
package calculator;

public enum Priority {
	PARENTHESES(10), MULTIPLTY(5), DIVIDE(5), ADD(2), SUBSTRCT(2);

	private final int value;

	private Priority(int value) {
		this.value = value;
	}

	public int getValue() {
		return value;
	}
	
}
```

**Operator.java**
```java
package calculator;

import java.util.Comparator;

public class Operator {
	public int getIdx() {
		return idx;
	}

	public void setIdx(int idx) {
		this.idx = idx;
	}

	public int getPriority() {
		return priority;
	}

	public void setPriority(int priority) {
		this.priority = priority;
	}

	public char getOp() {
		return op;
	}

	@Override
	public String toString() {
		return "Operator [idx=" + idx + ", priority=" + priority + ", op=" + op + "]";
	}

	public void setOp(char op) {
		this.op = op;
	}

	private int idx;
	private int priority;
	private char op;


}
```
**Calculator.java**
```java
package calculator;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Calculator {

	public static final char ADD = '+';
	public static final char SUBTRACT = '-';
	public static final char MULTIPLY = '*';
	public static final char DIVIDE = '/';

	private static List<Double> nums = new ArrayList<>();
	private static List<Operator> ops = new ArrayList<>();

	public static void main(String[] args) {

		String input = "5*3+(2-1)";
		int curIdx = 0;
		int curPriority = 0;
		StringBuilder curNum = new StringBuilder();
		for (int i = 0; i < input.length(); i++) {
			
			if (curPriority < 0) {
				System.err.println("left/right parentheses match failed");
				return;
			}
			
			char ch = input.charAt(i);
			if (isSpace(ch)) {
				continue;
			}

			if (isOperand(ch)) {
				curNum.append(ch);
			} else if (isOperator(ch)) {
				double v = Double.parseDouble(curNum.toString());
				curNum.setLength(0);
				nums.add(v);

				Operator op = new Operator();
				op.setIdx(curIdx++);
				op.setOp(ch);
				if (ch == ADD) {
					op.setPriority(curPriority + Priority.ADD.getValue());
				} else if (ch == SUBTRACT) {
					op.setPriority(curPriority + Priority.SUBSTRCT.getValue());
				} else if (ch == MULTIPLY) {
					op.setPriority(curPriority + Priority.MULTIPLTY.getValue());
				} else if (ch == DIVIDE) {
					op.setPriority(curPriority + Priority.DIVIDE.getValue());
				} else {
					// NOTHING TODO
				}
				ops.add(op);
			} else if (isParentheses(ch)) {

				if (ch == '(') {
					curPriority += Priority.PARENTHESES.getValue();
				} else {
					curPriority -= Priority.PARENTHESES.getValue();
				}
				continue;

			} else {
				System.err.printf("invalid character:%s\n", ch);
				return;
			}

		}
		if (curPriority != 0) {
			System.err.println("left/right parentheses match failed");
			return;
		}

		
		if (curNum.length() > 0) {
			double v = Double.parseDouble(curNum.toString());

			nums.add(v);
		}

		Collections.sort(ops, new Comparator<Operator>() {

			@Override
			public int compare(Operator arg0, Operator arg1) {
				return arg1.getPriority() - arg0.getPriority();
			}
		});
		double result = 0;
		for (Operator op : ops) {
			int leftIdx = op.getIdx();
			int rightIdx = op.getIdx() + 1;

			Double leftNum = nums.get(leftIdx);
			Double rightNum = nums.get(rightIdx);

			result = calculate(leftNum, rightNum, op);
			nums.set(rightIdx, result);
			nums.set(leftIdx, result);

		}
		System.out.printf("%s=%f", input, result);
	}

	public static double calculate(double left, double right, Operator op) {
		if (op.getOp() == ADD) {
			return left + right;
		} else if (op.getOp() == SUBTRACT) {
			return left - right;
		} else if (op.getOp() == MULTIPLY) {
			return left * right;
		} else if (op.getOp() == DIVIDE) {
			return left / right;
		} else {
			return 0.0;
		}
	}

	public static boolean isParentheses(char ch) {
		if (ch == '(' || ch == ')') {
			return true;
		}
		return false;
	}

	public static boolean isSpace(char ch) {
		if (Character.isSpaceChar(ch)) {
			return true;
		}
		return false;
	}

	public static boolean isOperand(char ch) {
		if (Character.isDigit(ch)) {
			return true;
		}
		return false;
	}

	public static boolean isOperator(char ch) {
		if (ch == ADD || ch == SUBTRACT || ch == MULTIPLY || ch == DIVIDE) {
			return true;
		}
		return false;

	}
}
```
