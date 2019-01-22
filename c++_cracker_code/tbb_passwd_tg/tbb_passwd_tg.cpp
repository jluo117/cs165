#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdarg.h>
#include <assert.h>

#include <iostream>
#include <string>
//#include <tr1/regex>
#include <regex>
#include <map>

#include "tbb/tick_count.h"
#include "tbb/spin_mutex.h"
#include "tbb/task_group.h"
#include "tbb/tbb_thread.h"

#include "md5.h"

#define MD5_DIGEST_SIZE 16

// global data
std::map<std::string, std::string> mapTeamData;
std::string salt;
std::string magic;

// timing
tbb::tick_count t0;

// call counter
tbb::atomic<unsigned> call_counter;

// helpers
void comment(char*fmt, ...)
{
    va_list     arg;
    va_start(arg, fmt);

    char szBuf[4096];
    vsnprintf(szBuf, sizeof(szBuf), fmt, arg);

    printf(szBuf);
    va_end(arg);
}

int performance()
{
    // collect timing
    tbb::tick_count t1 = tbb::tick_count::now();
    int nSeconds = (int)(t1 - t0).seconds();
    return (unsigned int)call_counter / (nSeconds > 0 ? nSeconds : 1);
}

// hash monster
void getHash(const std::string &password, const std::string &salt, const std::string &magic, std::string &hash)
{
    MD5 md5Alt;
    md5Alt.update(password.c_str(), password.length());
    md5Alt.update(salt.c_str(), salt.length());
    md5Alt.update(password.c_str(), password.length());
    unsigned char *pD = md5Alt.finalize().getDigest();
    // attach digest
    std::string sInter(password + magic + salt);
    for (int i = 0; i < password.length(); i++)
        sInter += pD[i % MD5_DIGEST_SIZE];

    for (std::size_t nPL = password.length(); nPL; nPL >>= 1)
    {
        if (nPL & 1)
            sInter.append(1, 0);
        else
            sInter += password[0];
    }

    // intermediate
    MD5 md5Inter(sInter);
    sInter.assign((const char*)md5Inter.getDigest(), MD5_DIGEST_SIZE);

    // stretching
    for (int i = 0; i < 1000; i++)
    {
        MD5 md5Next;

        if (i % 2)
            md5Next.update(password.c_str(), password.length());
        else
            md5Next.update(sInter.c_str(), sInter.length());

        if (i % 3)
            md5Next.update(salt.c_str(), salt.length());

        if (i % 7)
            md5Next.update(password.c_str(), password.length());

        if (i % 2 == 0)
            md5Next.update(password.c_str(), password.length());

        if (i % 2)
            md5Next.update(sInter.c_str(), sInter.length());

        sInter.assign((const char*)md5Next.finalize().getDigest(), MD5_DIGEST_SIZE);
    }

    // reorder
    int md5CryptSwaps[] = { 12, 6, 0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 5, 10, 4, 11 };
    int md5CryptSwapsLen = sizeof(md5CryptSwaps) / sizeof(int);
    // decode
    char *CryptBase = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    //
    unsigned v = 0;
    unsigned bits = 0;
    for (int i = 0; i < md5CryptSwapsLen; i++)
    {
        unsigned u = sInter[md5CryptSwaps[i]] & 0xff;
        v |= u << bits;
        bits += 8;
        while (bits > 6)
        {
            int nCBIdx = v & 0x03f;
            char chCB = CryptBase[nCBIdx];

            hash.append(1, chCB);

            v >>= 6;
            bits -= 6;
        }
    }

    // padding
    char chCB = CryptBase[v & 0x03f];
    hash.append(1, chCB);
}

// main work func
void passCrack(const std::string &password)
{
    std::string hash;
    getHash(password, salt, magic, hash);

    std::map<std::string, std::string>::iterator it = mapTeamData.find(hash);

    if (it != mapTeamData.end())
    {
        // password matches hash
        std::string sHash = it->first;
        std::string sTeam = it->second;

        comment("%10.10s : %-10.10s  throughput %d/second\n",
            sTeam.c_str(), password.c_str(), performance());
    }

    // update performance counter
    unsigned cntr = call_counter.fetch_and_increment();

# if 1
    if (cntr && cntr % 1000 == 0)
    {
        comment("tested %d K,  throughput %d/second\n",
            (unsigned)(cntr / 1000), performance());
    }
#endif
}

// get password combo
bool getPassCombo(std::string &sPass)
{
#define MAX_PASS_LENGTH 6
#define DICT_LENGTH 26

    static int idxs[MAX_PASS_LENGTH + 1] = { 0 };
    static int idx = 0;
    static char *sDict = "abcdefghijklmnopqrstuvwxyz";
    static tbb::spin_mutex mtx;

    // clear buffer
    sPass.clear();
    // lock the mtx
    mtx.lock();
    // end of the sequence
    if (idx < MAX_PASS_LENGTH)
    {
        // build string phase
        for (int i = 0; i <= idx; i++)
            sPass.append(1, sDict[idxs[i]]);

        // advance phase
        idxs[0]++;
        for (int i = 0; i < MAX_PASS_LENGTH; i++)
        {
            if (idxs[i] == DICT_LENGTH)
            {
                idxs[i] = 0;
                if (idx < i + 1)
                    idx = i + 1;
                else
                    idxs[i + 1]++;
            }
            else
                break;
        }
    }
    // unlock the mtx
    mtx.unlock();

    return !sPass.empty();
}

// 
int main(int argc, char *argv[])
{
    // sanity check
    std::string hash;
    getHash(std::string("password"), std::string("hfT7jp2q"), std::string("$1$"), hash);

    if (hash != "G3yf0NUx7mUkX.LIFWQxN.")
    {
        comment("Sanity check failed. Exiting...\n");
        return 1;
    }

    // load and parse all data from stdin ( < etc_shadow)
    comment("Please, enter data from etc_shadow\n\n");;
    //
    std::smatch sm;
    std::regex e("([^:]+):([^:]+).*\r*");
    //
    std::smatch sm2;
    std::regex e2("(\\$\\d\\$)([^\\$]+)\\$(.*)");

    for (;;)
    {
        std::string sData;
        std::getline(std::cin, sData);
        if (sData == "")
            break;

        if (std::regex_match(sData, sm, e))
        {
            std::string sTeam = sm[1];
            std::string sFullHash = sm[2];

            if (std::regex_match(sFullHash, sm2, e2))
            {
                std::string sMagic = sm2[1];
                magic = sMagic;
                std::string sSalt = sm2[2];
                salt = sSalt;
                std::string sHash = sm2[3];
                mapTeamData[sHash] = sTeam;

                std::cout << sTeam << " : " << sHash << std::endl;
            }
        }
    }

    //
    unsigned nCPUs = tbb::tbb_thread::hardware_concurrency();
    comment("\n\nStarting process for %d CPUs ...\n\n", nCPUs);
    tbb::task_group g;
    // capture time
    t0 = tbb::tick_count::now();
    // load all available cores
    for (unsigned nCPU = 0; nCPU < nCPUs; nCPU++)
    {
        // add task to a group and run
        g.run([]() {
            std::string password;
            while(getPassCombo(password))
                passCrack(password);
        });
    }
    // wait for all tasks in the group to finish
    g.wait();
    // final report
    int nSeconds = (int)(tbb::tick_count::now() - t0).seconds();
    comment("\n\nDone. Tried %d combinations in %d seconds, troughput %d/second\n",
        (unsigned)call_counter, nSeconds, performance());
}