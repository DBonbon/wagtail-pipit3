// import PropTypes from 'prop-types';
import Link from 'next/link';
import Head from 'next/head';
import Image from 'next/image';
import s from './Layout.module.css';
import utilStyles from '../../styles/utils.module.css';
import Logo from '../../public/img/logo-no-background.svg';
import { Card, Text } from "@nextui-org/react";


export const siteTitle = 'Next.js Sample Website';

const Layout = ({text, name, children, home}) => (
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
