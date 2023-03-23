// import PropTypes from 'prop-types';
import Head from 'next/head';
import Link from 'next/link';
import Image from 'next/image';
import {AcmeLogo} from '../AcmeLogo/AcmeLogo.js'
import s from './Layout.module.css';
import utilStyles from '../../styles/utils.module.css';
import Logo from '../../public/img/logo-no-background.svg';
import { Avatar } from '@nextui-org/react';
import { Navbar, Button, Text, Card, Radio } from "@nextui-org/react";

export const siteTitle = 'Next.js Sample Website';


const Layout = ({name, children, home}) => (
    <div className={s.container}>
      <Head>
        <link rel="icon" href="/favicon.ico" />
        <meta
          name="description"
          content="Learn how to build a personal website using Next.js"
        />
        <meta
          property="og:image"
          content={`https://og-image.vercel.app/${encodeURI(
            siteTitle,
          )}.png?theme=light&md=0&fontSize=75px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fnextjs-black-logo.svg`}
        />
        <meta name="og:title" content={siteTitle} />
        <meta name="twitter:card" content="summary_large_image" />
      </Head>






<Navbar>
        <Navbar>
        <Navbar.Brand>
          <AcmeLogo />
          <Avatar
          squared
          src="https://i.pravatar.cc/150?u=a042581f4e29026024d" />
          <p color="inherit" hideIn="xs">
            ACME
          </p>
        </Navbar.Brand>

        <Navbar.Content hideIn="xs">
          <Navbar.Link href="#">Features</Navbar.Link>
          <Navbar.Link isActive href="#">Customers</Navbar.Link>
          <Navbar.Link href="#">Pricing</Navbar.Link>
          <Navbar.Link href="#">Company</Navbar.Link>
        </Navbar.Content>

          <Navbar>
            <Button auto flat as={Link} href="#">
              Sign Up
            </Button>
          </Navbar>
        </Navbar>
      </Navbar>

      <header className={s.header}>
        {home ? (
          <>
            <Image
              priority
              src="/img/profile.jpg"
              className={utilStyles.borderCircle}
              height={144}
              width={144}
              alt=""
            />
            <h1 className={utilStyles.heading2Xl}>{name}</h1>
          </>
        ) : (
          <>
            <Link href="/">
              <Image
                priority
                src="/img/profile.jpg"
                className={utilStyles.borderCircle}
                height={108}
                width={108}
                alt=""
              />
            </Link>
            <h2 className={utilStyles.headingLg}>
              <Link href="/" className={utilStyles.colorInherit}>
                {name}
              </Link>
            </h2>
          </>
        )}
      </header>
        <Avatar
          squared
          text="Junior" />
          <Avatar
          squared
          src="https://i.pravatar.cc/150?u=a042581f4e29026024d" />
      <Card
      isPressable
      isHoverable
      variant="bordered"
      css={{ mw: "400px" }}
    >
      <Card.Body>
        <Text>A pressable card.</Text>
      </Card.Body>
    </Card>


      <main>{children}</main>
      {!home && (
        <div className={s.backToHome}>
          <Link href="/">← Back to home</Link>
        </div>
      )}
    </div>
);

Layout.propTypes = {};

Layout.defaultProps = {};

export default Layout;
