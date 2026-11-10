import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama import ChatOllama
from langchain_anthropic import ChatAnthropic

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")


def main() -> None:
    print("Hello from langchain-course!")
    information = """Crete (/kriːt/ KREET)[a] is the largest and most populous island of Greece, the 89th largest island in the world, and the fifth largest island in the Mediterranean Sea, after Sicily, Sardinia, Cyprus, and Corsica. Crete is located approximately 100 km (62 mi) south of the Peloponnese, and about 300 km (190 mi) southwest of Anatolia. Crete has an area of 8,450 km2 (3,260 mi2) and a coastline of 1,046 km (650 mi). It bounds the southern border of the Aegean Sea, with the Sea of Crete (or North Cretan Sea) to the north and the Libyan Sea (or South Cretan Sea) to the south. Crete covers 260 km from west to east but is narrow from north to south, spanning three degrees of longitude but only half a degree of latitude.

    Crete and its surrounding islands and islets form the Region of Crete (Greek: Περιφέρεια Κρήτης), which is the southernmost of the 13 top-level administrative units of Greece, and the fifth most populous of Greece's regions. Its capital and largest city is Heraklion, located on the island's north shore. As of 2021, the region had a population of 624,408.[4] The Dodecanese are located to the northeast of Crete, while the Cyclades are situated to the north, separated by the Sea of Crete.

    Crete was the centre of Europe's first advanced civilization, the Minoans, from 2700 to 1420 BCE. The Minoan civilisation was overrun by the Mycenaean civilization from mainland Greece. Crete was subsequently ruled by Rome, by the Byzantine Empire, briefly by Andalusian Arabs, restored to Byzantine rule, and later by the Venetian Republic and the Ottoman Empire. In 1898 Crete, whose people had for some time wanted to join the Greek state, achieved autonomy under the Ottomans, formally becoming the Cretan State. Crete became part of Greece in December 1913.

    Crete is predominantly mountainous, characterised by a range that crosses the island from west to east. It includes Crete's highest point, Mount Ida, and the range of the White Mountains (Lefka Ori) with 30 summits above 2,000 metres (6,600 ft) in altitude and the Samaria Gorge, a World Biosphere Reserve. Crete forms a significant part of the economy and cultural heritage of Greece, while retaining its own local cultural traits (such as its own poetry and music). The Nikos Kazantzakis airport at Heraklion and the Daskalogiannis airport at Chania serve international travellers. The Minoan palace at Knossos is also located in Heraklion.[5] In Greek mythology, Crete is best known as the birthplace of the Greek god Zeus.

    Name
    This section contains Linear B Unicode characters. Without proper rendering support, you may see question marks, boxes, or other symbols instead of Linear B.
    kA
    Z1	I9	U33	Z7	N25
    Crete
    Keftiu
    in hieroglyphs
    The earliest references to the island of Crete come from texts from the Syrian city of Mari dating from the 18th century BC, where the island is referred to as Kaptara.[6] This is repeated later in Neo-Assyrian records and the Bible (Caphtor). It was known in ancient Egyptian as Keftiu or kftı͗w, strongly suggesting a similar Minoan name for the island.[7]

    The current name Crete is first attested in the 15th century BC in Mycenaean Greek texts, written in Linear B, through the words ke-re-te 𐀐𐀩𐀳, *Krētes; later Greek: Κρῆτες [krɛː.tes], plural of Κρής [krɛːs])[8] and ke-re-si-jo 𐀐𐀩𐀯𐀍, *Krēsijos; later Greek: Κρήσιος [krέːsios],[9] 'Cretian').[10][11] In Ancient Greek, the name Crete (Κρήτη) first appears in Homer's Odyssey.[12] Its etymology is unknown. One proposal derives it from a hypothetical Luwian word *kursatta (compare kursawar 'island', kursattar 'cutting, sliver').[13] Another proposal suggests that it derives from the ancient Greek word "κραταιή" (krataie̅), meaning strong or powerful, the reasoning being that Crete was the strongest thalassocracy during ancient times.[14][15]

    In Latin, the name of the island became Creta. The original Arabic name of Crete was Iqrīṭiš (Arabic: اقريطش < (τῆς) Κρήτης), but after the Emirate of Crete's establishment of its new capital at ربض الخندق Rabḍ al-Ḫandaq (modern Heraklion; Greek: Ηράκλειο, Irákleio), both the city and the island became known as Χάνδαξ (Chandax) or Χάνδακας (Chandakas), which gave Latin, Italian, and Venetian Candia, from which were derived French Candie and English Candy or Candia. Under Ottoman rule, in Ottoman Turkish, Crete was called Girit (كريد). In the Hebrew Bible, Crete is referred to as כְּרֵתִים "kretim", in the plural, reflecting its multiple island nature[clarification needed] (cf. קפריסין "kafrisin" Cyprus) and as כפתור "kaftor", mirroring both names."""

    summary_template = """
    Given the following {information} about a country, please provide
    1.  a short summary
    2. interesting facts about the country
    
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")
    # llm = ChatOllama(model="gemma3:270m", temperature=0)

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
