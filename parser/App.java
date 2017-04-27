package genomics;
/*
 * GFF and Fasta parser using biojava
 */

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

import org.biojava.nbio.core.sequence.ChromosomeSequence;
import org.biojava.nbio.core.sequence.ProteinSequence;
import org.biojava.nbio.core.sequence.io.FastaWriterHelper;
import org.biojava.nbio.genome.GeneFeatureHelper;
import org.biojava.nbio.genome.parsers.gff.GFF3Reader;
import org.biojava.nbio.genome.parsers.gff.FeatureI;
import org.biojava.nbio.genome.parsers.gff.FeatureList;
import org.biojava.nbio.core.sequence.*;


public class App 
{
    public static void main( String[] args )
    {

    	parseGFF("/Users/hbagheri/Documents/bio/protozoa/gff/GCF_000002415.2_ASM241v2_genomic.gff");
    	 
    	parseFasta("/Users/hbagheri/Documents/bio/protozoa/GCF_000002415.2_ASM241v2_genomic.fna");

    }

	private static void parseFasta(String string) {

		
	}

	public static void parseGFF(String strFile) {
		try {
    		FeatureList f = GFF3Reader.read(strFile);
    		
    		//seqName= f.selectByGroup("seqname");
    		
    		Set<String> accSet= new HashSet<String>();
    		
    		f.attributeValues("seqname");
    		for(FeatureI feature: f){
//    			System.out.println( "seqName: " + feature.seqname());
//    			System.out.println( "type: " + feature.type());
//    			System.out.println( "location: " + feature.location());

    			accSet.add(feature.seqname());

    			String[] rec =feature.toString().split("\t");

    			//System.out.println( rec[0]+ "__" + rec[1]+ "__"+ rec[2]+ "__" + rec[3]+ "__" + rec[4]+ "__"+ rec[5]+ "__");

    			System.out.println(feature);
    			for (Map.Entry<String, String> entry: feature.getAttributes().entrySet()){
    				System.out.println("		attribute: " + entry.getKey() + " value: "+ entry.getValue());
    			}
    		}
    		
    		System.out.println("SeqName Size: " + accSet.size());
    		
    	} catch (IOException e) {
    		// TODO Auto-generated catch block
    		e.printStackTrace();
    	}
			}
	
 
	
}
