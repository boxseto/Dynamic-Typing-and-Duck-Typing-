/*
 * CSCI3180 Principles of Programming Languages
 *
 * --- Declaration ---
 *
 * I declare that the assignment here submitted is original except for source
 * material explicitly acknowledged. I also acknowledge that I am aware of
 * University policy and regulations on honesty in academic work, and of the
 * disciplinary guidelines and procedures applicable to breaches of such policy
 * and regulations, as contained in the website
 * http://www.cuhk.edu.hk/policy/academichonesty/
 *
 * Assignment 2
 * Name : Seto Tsz Kin
 * Student ID : 1155092585
 * Email Addr : 1155092585@link.cuhk.edu.hk
 */
 public class Potion extends NPC {

 	private static final int AID_CAP = 10;
 	public Potion(int posx, int posy, int index, Map map) {
 		super(posx, posy, index, map);
 		this.setName("P" + Integer.toString(index));
 		this.setPower(TheJourney.rand.nextInt(AID_CAP - 5) + 5);
 	}

  public boolean actionOnWarrior(Warrior warrior) {
    warrior.talk("Very good, I got additional healing potion "+ this.getName() +".");
    warrior.increaseHealth(this.getPower());
    this.map.decreaseNumOfPotion();
    this.map.deleteTeleportableObj(this);
    return true;
  }


 }
