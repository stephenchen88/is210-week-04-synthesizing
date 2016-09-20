#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fahrenheit to Celsius."""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """converting a Fahrenheit temperature to Celsius.
    Args:
        degrees (mixed): Degree in Fahrenheit.
    Returns:
        decimal: Degree in Celsius.
    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')
        >>> fahrenheit_to_celsius('26.389')
        Decimal('-3.117222222222222222222222222')
    """
    degrees = decimal.Decimal(degrees)
    degrees = (degrees - 32) * 5 / 9
    return degrees


def celsius_to_kelvin(degrees):
    """converting a Celsius temperature to Kelvin.
    Args:
        degrees (mixed): Degree in Celsius.
    Returns:
        decimal: Degree in Kelvin.
    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')
        >>> celsius_to_kelvin(50)
        Decimal('323.15')
    """
    degrees = degrees + ABSOLUTE_DIFFERENCE
    return degrees


def fahrenheit_to_kelvin(degrees):
    """converting a Fahrenheit temperature to Kelvin.
    Args:
        degrees (mixed): Degree in Fahrenheit.
    Returns:
        decimal: Degree in Kelvin.
    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')
        >>> fahrenheit_to_kelvin(100)
        Decimal('310.9277777777777777777777778')
    """
    degrees = fahrenheit_to_celsius(degrees)
    degrees = celsius_to_kelvin(degrees)
    return degrees
