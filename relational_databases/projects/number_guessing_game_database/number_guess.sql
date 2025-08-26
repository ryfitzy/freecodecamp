--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE number_guess;
--
-- Name: number_guess; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE number_guess WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE number_guess OWNER TO freecodecamp;

\connect number_guess

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: users; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.users (
    username character varying(22) NOT NULL,
    games_played integer DEFAULT 0 NOT NULL,
    best_game integer
);


ALTER TABLE public.users OWNER TO freecodecamp;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.users VALUES ('user_1756239921279', 2, 246);
INSERT INTO public.users VALUES ('user_1756240041090', 2, 140);
INSERT INTO public.users VALUES ('user_1756239921280', 5, 21);
INSERT INTO public.users VALUES ('user_1756240041091', 5, 7);
INSERT INTO public.users VALUES ('user_1756239928297', 2, 251);
INSERT INTO public.users VALUES ('user_1756240069591', 2, 546);
INSERT INTO public.users VALUES ('user_1756239928298', 5, 27);
INSERT INTO public.users VALUES ('user_1756239991491', 2, 181);
INSERT INTO public.users VALUES ('user_1756240044984', 2, 736);
INSERT INTO public.users VALUES ('user_1756240069592', 5, 235);
INSERT INTO public.users VALUES ('user_1756239991492', 5, 103);
INSERT INTO public.users VALUES ('user_1756240044985', 5, 8);
INSERT INTO public.users VALUES ('user_1756239996151', 2, 885);
INSERT INTO public.users VALUES ('user_1756239996152', 5, 177);
INSERT INTO public.users VALUES ('user_1756240049713', 2, 9);
INSERT INTO public.users VALUES ('user_1756239999548', 2, 449);
INSERT INTO public.users VALUES ('user_1756240071382', 2, 26);
INSERT INTO public.users VALUES ('user_1756239999549', 5, 202);
INSERT INTO public.users VALUES ('user_1756240049714', 5, 323);
INSERT INTO public.users VALUES ('user_1756240005145', 2, 410);
INSERT INTO public.users VALUES ('user_1756240005146', 5, 70);
INSERT INTO public.users VALUES ('user_1756240071383', 5, 32);
INSERT INTO public.users VALUES ('user_1756240051350', 2, 448);
INSERT INTO public.users VALUES ('user_1756240008503', 2, 141);
INSERT INTO public.users VALUES ('user_1756240051351', 5, 374);
INSERT INTO public.users VALUES ('user_1756240008504', 5, 110);
INSERT INTO public.users VALUES ('user_1756240012767', 2, 321);
INSERT INTO public.users VALUES ('user_1756240012768', 5, 142);
INSERT INTO public.users VALUES ('user_1756240053173', 2, 152);
INSERT INTO public.users VALUES ('user_1756240018527', 2, 320);
INSERT INTO public.users VALUES ('user_1756240053174', 5, 369);
INSERT INTO public.users VALUES ('user_1756240018528', 5, 31);
INSERT INTO public.users VALUES ('user_1756240022871', 2, 505);
INSERT INTO public.users VALUES ('user_1756240054873', 2, 223);
INSERT INTO public.users VALUES ('user_1756240022872', 5, 179);
INSERT INTO public.users VALUES ('user_1756240054874', 5, 128);
INSERT INTO public.users VALUES ('user_1756240035055', 2, 840);
INSERT INTO public.users VALUES ('user_1756240035056', 5, 535);
INSERT INTO public.users VALUES ('user_1756240036878', 2, 156);
INSERT INTO public.users VALUES ('user_1756240056496', 2, 423);
INSERT INTO public.users VALUES ('user_1756240036879', 5, 32);
INSERT INTO public.users VALUES ('user_1756240056497', 5, 38);
INSERT INTO public.users VALUES ('user_1756240038366', 2, 862);
INSERT INTO public.users VALUES ('user_1756240038367', 5, 186);
INSERT INTO public.users VALUES ('user_1756240058108', 2, 195);
INSERT INTO public.users VALUES ('user_1756240039754', 2, 415);
INSERT INTO public.users VALUES ('user_1756240039755', 5, 33);
INSERT INTO public.users VALUES ('user_1756240058109', 5, 132);
INSERT INTO public.users VALUES ('user_1756240059799', 2, 310);
INSERT INTO public.users VALUES ('user_1756240059800', 5, 228);
INSERT INTO public.users VALUES ('user_1756240061264', 2, 24);
INSERT INTO public.users VALUES ('user_1756240061265', 5, 418);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

