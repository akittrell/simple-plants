CREATE TABLE public.plants (
	id bigint GENERATED ALWAYS AS IDENTITY,
	family_name varchar NOT NULL,
	genus varchar NULL,
	common_name varchar NULL,
	CONSTRAINT plants_pk PRIMARY KEY (id)
);
