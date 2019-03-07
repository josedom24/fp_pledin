---
title: "Ejercicio Esquemas XML: Biblioteca"
permalink: /lmgs/u04/esquema.html
---

La herramienta de validación desde línea de comandos que utilizaremos se llama `xmllint`, que pertenece al paquete debian `libxml2-utils` Para validar un fichero xml con un fichero XSD (XML Schema Definition) ejecutamos el siguiente comando:

	xmllint fichero.xml --schema fichero.xsd

Tambien podemos utilizar un programa gráfico que se llama xsddiagram.

## Ejemplo 1: Tipos simples

ejemplo1.xml

	<?xml version="1.0" encoding="utf-8"?>
	<nota>hola</nota>

ejemplo1.xsd

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
		<xs:element name="nota" type="xs:string"/>
	</xs:schema>

## Ejemplo 2: Tipos complejos

[libro1.xml](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro1.xml)

	<libro>
		<autor>Miguel de Cervantes Saavedra</autor>
		<titulo>El Quijote de la Mancha</titulo>
	</libro>

[libro1.xsd](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro1.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="libro">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="autor" type="xs:string" />
				<xs:element name="titulo" type="xs:string" />
			</xs:sequence>
		</xs:complexType>
		</xs:element>
	</xs:schema>

## Ejemplo 3: Tipos complejos II

[libro2.xml](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro2.xml)

	<biblioteca>
		<libro>
			<autor>Miguel de Cervantes Saavedra</autor>
			<titulo>El Quijote de la Mancha</titulo>
		</libro>
		<libro>
			<autor>Pablo Neruda</autor>
			<titulo>Veinte poemas de amor y una canción desesperada</titulo>
		</libro>
	</biblioteca>

[libro2.xsd](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro2.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="biblioteca">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="libro" minOccurs="0" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="autor" />
							<xs:element name="titulo" />
						</xs:sequence>
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	</xs:schema>

## Ejemplo 4: Restricciones

[libro3.xml](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro3.xml)

	<?xml version="1.0" encoding="utf-8"?>
	<biblioteca>
		<libro>
			<autor>Miguel de Cervantes Saavedra</autor>
			<titulo>El Quijote de la Mancha</titulo>
			<codigo>123</codigo>
	    </libro>
	  	<libro>
	  		<autor>Pablo Neruda</autor>
	  		<titulo>Veinte poemas de amor y una canción desesperada</titulo>
	  		<codigo>124</codigo>
	  	</libro>
	</biblioteca>

[libro3.xsd](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro3.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="biblioteca">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="libro" minOccurs="0" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="autor" />
							<xs:element name="titulo" />
							<xs:element name="codigo">
								<xs:simpleType>
									<xs:restriction base="xs:integer">
										<xs:minInclusive value="1"/>
										<xs:maxInclusive value="9999"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	</xs:schema>

## Ejemplo 5: Restricciones II

[libro4.xml](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro4.xml)

	<?xml version="1.0" encoding="utf-8"?>
	<biblioteca>
		<libro>
			<autor>Miguel de Cervantes Saavedra</autor>
			<titulo>El Quijote de la Mancha</titulo>
			<codigo>123</codigo>
			<ubicacion>estantería 1</ubicacion>
		</libro>
		<libro>
			<autor>Pablo Neruda</autor>
			<titulo>Veinte poemas de amor y una canción desesperada</titulo>
			<codigo>124</codigo>
			<ubicacion>estantería 11</ubicacion>
		</libro>
	</biblioteca>

[libro4.xsd](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro4.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="biblioteca">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="libro" minOccurs="0" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="autor" />
							<xs:element name="titulo" />
							<xs:element name="codigo">
								<xs:simpleType>
									<xs:restriction base="xs:integer">
										<xs:minInclusive value="1"/>
										<xs:maxInclusive value="9999"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
							<xs:element name="ubicacion">
								<xs:simpleType>
									<xs:restriction base="xs:string">
										<xs:enumeration value="estantería 1"/>
										<xs:enumeration value="estantería 2"/>
										<xs:enumeration value="estantería 3"/>
										<xs:enumeration value="estantería 4"/>
										<xs:enumeration value="estantería 5"/>
										<xs:enumeration value="estantería 6"/>
										<xs:enumeration value="estantería 7"/>
										<xs:enumeration value="estantería 8"/>
										<xs:enumeration value="estantería 9"/>
										<xs:enumeration value="estantería 10"/>
										<xs:enumeration value="estantería 11"/>
										<xs:enumeration value="estantería 12"/>
										<xs:enumeration value="estantería 13"/>
										<xs:enumeration value="estantería 14"/>
									</xs:restriction>
								</xs:simpleType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	</xs:schema>

## Ejemplo 6: Atributos

[libro5.xml](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro5.xml)

	<?xml version="1.0" encoding="utf-8"?>
	<biblioteca>
		<libro codigo="123" ubicacion="estantería 1">
			<autor>Miguel de Cervantes Saavedra</autor>
			<titulo>El Quijote de la Mancha</titulo>
		</libro>
		<libro codigo="1023" ubicacion="estantería 3">
			<autor>Pablo Neruda</autor>
			<titulo>Veinte poemas de amor y una canción desesperada</titulo>
		</libro>
	</biblioteca>

[libro5.xsd](https://raw.githubusercontent.com/josedom24/fp_pledin/master/modulos/_lmgs/lmgs/u04/fich/libro5.xsd)

	<?xml version="1.0" encoding="utf-8"?>
	<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xs:element name="biblioteca">
		<xs:complexType>
			<xs:sequence>
				<xs:element name="libro" minOccurs="0" maxOccurs="unbounded">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="autor" />
							<xs:element name="titulo" />
						</xs:sequence>
						<xs:attribute name="codigo">
							<xs:simpleType>
								<xs:restriction base="xs:integer">
									<xs:minInclusive value="1"/>
									<xs:maxInclusive value="9999"/>
								</xs:restriction>
							</xs:simpleType>
						</xs:attribute>
						<xs:attribute name="ubicacion">
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:enumeration value="estantería 1"/>
									<xs:enumeration value="estantería 2"/>
									<xs:enumeration value="estantería 3"/>
									<xs:enumeration value="estantería 4"/>
									<xs:enumeration value="estantería 5"/>
									<xs:enumeration value="estantería 6"/>
									<xs:enumeration value="estantería 7"/>
									<xs:enumeration value="estantería 8"/>
									<xs:enumeration value="estantería 9"/>
									<xs:enumeration value="estantería 10"/>
									<xs:enumeration value="estantería 11"/>
									<xs:enumeration value="estantería 12"/>
									<xs:enumeration value="estantería 13"/>
									<xs:enumeration value="estantería 14"/>
								</xs:restriction>
							</xs:simpleType>
						</xs:attribute>
					</xs:complexType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
	</xs:element>
	</xs:schema>
