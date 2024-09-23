CREATE TABLE public.plants (
	id varchar NOT NULL,
	family_name varchar NOT NULL,
	genus varchar NULL,
	common_name varchar NULL,
	CONSTRAINT plants_pk PRIMARY KEY (id)
);
